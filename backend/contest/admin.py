from django.contrib import admin
from .models import Contest, Video
from video_encoding.admin import FormatInline
# Register your models here.


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
   inlines: (FormatInline,)
   list_display = ('file', 'contest', 'duration', 'height', 'width')
   fields = ('file', 'contest')


admin.site.register(Contest)
