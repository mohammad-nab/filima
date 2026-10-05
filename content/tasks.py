from celery import shared_task
from content.models import VideoContent
import subprocess
import os
import tempfile
import json
from .models import ProcessedVideo
from django.core.files import File
from django.core.files.storage import default_storage



def convert_video(input_path, output_path, height):
    subprocess.run(
        [
            "ffmpeg",
            "-i", input_path,
            "-vf", f"scale=-2:{height}",
            "-c:v", "libx264",
            "-c:a", "aac",
            "-y",
            output_path,
        ],
        check=True,
    )

@shared_task
def process_video(video_uuid):
    video_content = VideoContent.objects.get(video_uuid=video_uuid)

    with video_content.video.open("rb") as video_file:
        with tempfile.NamedTemporaryFile(
            suffix=os.path.splitext(video_content.video.name)[1],
            delete=False,
        ) as temp_file:

            temp_file.write(video_file.read())
            temp_path = temp_file.name

    try:

        result = subprocess.run(
            [
                "ffprobe",
                "-v", "error",
                "-show_format",
                "-show_streams",
                "-of", "json",
                temp_path,
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        metadata = json.loads(result.stdout)

        video_stream = next(
            stream for stream in metadata["streams"]
            if stream["codec_type"] == "video"
        )

        width = video_stream["width"]
        height = video_stream["height"]
        codec = video_stream["codec_name"]
        fps = video_stream["r_frame_rate"]
        duration = float(video_stream["duration"])

        qualities = [480, 360]
        qualities = [quality for quality in qualities if quality <= height]

        print("Source height:", height)
        print("Qualities to generate:", qualities)

        for quality in qualities:
            with tempfile.NamedTemporaryFile(
                    suffix=".mp4",
                    delete=False,
            ) as output_file:
                output_path = output_file.name

            try:
                convert_video(temp_path, output_path, quality)

                output_name = f"videos/processed/{video_uuid}_{quality}p.mp4"

                with open(output_path, "rb") as output_file:
                    saved_path = default_storage.save(
                        output_name,
                        File(output_file),
                    )
                    ProcessedVideo.objects.create(
                        video_content= video_content,
                        quality=quality,
                        file=saved_path
                    )

                print(f"{quality}p video uploaded:", saved_path)

            finally:
                if os.path.exists(output_path):
                    os.remove(output_path)


    finally:
        os.remove(temp_path)