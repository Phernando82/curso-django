from django.shortcuts import render

class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.vimeo_id = vimeo_id
        self.titulo = titulo

videos = [
    Video('u2', 'Video Aperitivo: U2', 710132185),
    Video('desafio', 'Desafio Dev Pro', 711175523),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
