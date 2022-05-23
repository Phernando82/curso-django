from django.shortcuts import render, get_object_or_404

from pypro.aperitivos.models import Video

videos = [
    Video(slug='u2', titulo='Video Aperitivo: U2', vimeo_id='710132185'),
    Video(slug='desafio', titulo='Desafio Dev Pro', vimeo_id='711175523'),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
