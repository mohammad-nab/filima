from celery import shared_task
from content.models import VideoContent


@shared_task
def process_video(video_uuid):
    video_content = VideoContent.objects.get(video_uuid=video_uuid)

    return f"Processing video: {video_content.video.name}"
