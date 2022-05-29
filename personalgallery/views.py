from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image, Location,Category

# Create your views here.
def index(request):
    # #CREATE THE ATIVE LINKS FOR CATGORY
    # category=request.GET.get('category')
    # if category == None:
    #     images = Image.objects.all()
    # else:
    #     images=Image.objects.filter(category__name=category)
    #CREATE THE ACTIVE LINKS FOR LOCATION  
    location=request.GET.get('location')
    if location == None:
        images=Image.objects.all()
    else: 
        images=Image.objects.filter(location__name=location)

    categories=Category.objects.all()
    location=Location.objects.all()
    return render(request, 'personalgallery/index.html', {"images":images, "categories": categories, "location":location})
