from django.contrib import admin
from .models import Contest, Video
from video_encoding.admin import FormatInline
# Register your models here.


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
   inlines = (FormatInline,)
   list_dispaly = ('get_filename', 'width', 'height', 'duration', 'contest')
   readonly_fields = ('width', 'height', 'duration')


admin.site.register(Contest)
