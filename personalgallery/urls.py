from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#app urls 
urlpatterns=[
    path('', views.index, name="indexpage"),
    path('search/', views.show_category, name="search_categories"),
    path('oneimage/<int:pk>', views.viewPhoto, name="viewPhoto"),
    path('searchbylocation/', views.show_by_location, name="showlocation")
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    # urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  