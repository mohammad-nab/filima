from celery import shared_task
from content.models import VideoContent
import subprocess
import os
import tempfile
import json
from django.core.files import File
from django.core.files.storage import default_storage


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
        output_file = tempfile.NamedTemporaryFile(
            suffix=".mp4",
            delete=False,
        )
        output_path = output_file.name
        output_file.close()

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

        subprocess.run(
            [
                "ffmpeg",
                "-i", temp_path,
                "-vf", "scale=-2:360",
                "-c:v", "libx264",
                "-c:a", "aac",
                "-y",
                output_path,
            ],
            check=True,
        )

        output_name = f"videos/processed/{video_uuid}_360p.mp4"

        with open(output_path, "rb") as output_file:
            saved_path = default_storage.save(
                output_name,
                File(output_file),
            )

        print("Processed video uploaded:", saved_path)

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

        print("Width:", width)
        print("Height:", height)
        print("Codec:", codec)
        print("FPS:", fps)
        print("Duration:", duration)


    finally:
        os.remove(temp_path)
        os.remove(output_path)