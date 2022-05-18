from django.shortcuts import render

def video(request, slug):
    video = {'titulo': 'Video Aperitivo: U2', 'vimeo_id': '710132185?h=c8686e2489'}
    return render(request, 'aperitivos/video.html', context={'video': video})
