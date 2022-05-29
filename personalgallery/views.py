
  
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

def viewPhoto(request, pk):
    image=Image.objects.get(id=pk)  
    return render(request, 'personalgallery/oneimage.html', {"image": image})

def show_category(request):
    if 'article' in request.GET and request.GET['article']:
        category=request.GET.get("article")
        searched_categories=Image.search_image(category)
        message=f"{category}"

        return render(request, 'personalgallery/search.html', {"message": message, "articles": searched_categories })
    else:
        message="You have not searched any category"
        return render(request, 'personalgallery/search.html', {"message":message})

def show_by_location(request):
    if 'places' in request.GET and request.GET['places']:
        location=request.GET.get('places')
        searched_locations=Image.filter_by_location(location)
        message = f"{location}"

        return render(request, 'personalgallery/searchlocation.html', {"message": message, "places": searched_locations})

    else:
        message="You have not searched any location"
        return render(request, 'personalgallery/searchlocation.html', {"message":message})