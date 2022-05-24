from django.contrib.admin import ModelAdmin, register

from pypro.aperitivos.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    List_display = ('titulo', 'slug', 'creation', 'vimeo_id')
