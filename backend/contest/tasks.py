from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail

from backend.celery import app
from video_encoding.tasks import convert_all_videos

from contest.models import Video, TaskManager


@app.task(queue='father')
def convert_videos():

    videos_to_convert = Video.objects.filter(status="En Proceso")
    if videos_to_convert.exists():
        app_label = videos_to_convert.first()._meta.app_label
        model_name = videos_to_convert.first()._meta.model_name
        for video in videos_to_convert:
            convert_video.delay( video.id, app_label, model_name)
            video.status = "converting"
            video.save()


@app.task(queue='son')
def convert_video(video_id, app_label, model_name):
    task_manager = TaskManager.objects.create(task_name='convert video: ' + video_id)
    convert_all_videos(app_label, model_name, video_id)
    task_manager.end_date = datetime.now()


@app.task(queue='check')
def check_videos():
    videos_in_converting_process = Video.objects.filter(status="converting")
    for video in videos_in_converting_process:
        video_url = settings.FRONT_URL + video.contest.url
        if video.format_set.complete().all().exists():
            video.status = "Convertido"
            video.save()
            send_mail('SmartTools - Video Cargado para conscurso','',
                      'c.cordobac@uniandes.edu.co',
                      [video.email],
                      html_message='El video que subiste para el concurso ' + video.contest.name +
                                   ' ha sido cargado con exito. Puedes ingresar a verlo en <a href'.format(
                                       video_url) + '>' + video_url,
                      fail_silently=False)
