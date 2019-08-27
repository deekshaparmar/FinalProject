from django.shortcuts import render
from Blog.models import Blogger
from About.models import Banner, aboutus

def index(request):
    context = {
        'Banners': Banner.objects.all(),
        'Blogs': Blogger.objects.all().order_by('-title')[:4],
        'About' : aboutus.objects.all()
    }

    return render(request, 'Main/index.html', context)

