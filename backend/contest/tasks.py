from backend.celery import app
from video_encoding.tasks import convert_all_videos

from contest.models import Video


@app.task()
def convert_video():
    videos_to_convert = Video.objects.all()
    print(videos_to_convert)
    app_label = videos_to_convert.first()._meta.app_label
    model_name = videos_to_convert.first()._meta.model_name
    for video in videos_to_convert:
        convert_all_videos(app_label, model_name, video.id)
