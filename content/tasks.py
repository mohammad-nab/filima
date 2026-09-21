from celery import shared_task
from content.models import VideoContent


@shared_task
def upload_content(video_uuid):
    video_content = VideoContent.objects.get(video_uuid=video_uuid)
