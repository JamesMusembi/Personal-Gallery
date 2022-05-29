from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Location(models.Model):
    name=models.CharField(max_length=400)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, name):
        self.update()

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=400)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, name):
        self.update()


    def __str__(self):
        return self.name

class Image(models.Model):
    image= models.ImageField(upload_to='articles/')
    image=CloudinaryField('image')
    image_name=models.CharField(max_length=400)
    description=models.TextField()
    location=models.ForeignKey(Location, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_category(self, image_name):
        self.update()


    def search_image(category):
        images=Image.objects.filter(category__name=category)
        # print(images)
        return images

    def filter_by_location(location):
        limages=Image.objects.filter(location__name=location)
        print(limages)
        return limages



    def __str__(self):
        return self.image_name