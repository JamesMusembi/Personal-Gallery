from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.

class ImageTestClass(TestCase):
    #setup method

    def setUp(self):

        #creating new location and saving it
        self.park=Location(name="park")
        self.park.save_location()

        #creating new category and saving it 
        self.outside = Category(name="outside")
        self.outside.save_category()
        
        #creating new image instance and saving it 
        self.image1 = Image(image="https://unsplash.com/photos/8ZfTxdPvNos", image_name='Elephant Portrait', description='Gorgeous close up image of an elephant', location=self.park, category=self.outside)
        self.image1.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image1, Image))

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_save_image(self):
        self.image1.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        images=Image.objects.all()

        self.image1.delete_image()
        self.assertEqual(len(images), 0)

    def test_update_image(self):
        self.image1.save_image()
        Image.objects.filter(image_name="Elephant Portrait").update(image_name='image2')
        self.assertTrue(Image.objects.get(image_name="image2"))


class LocationTestClass(TestCase):

    #setUpmethod
    def setUp(self):
        self.park=Location(name="park")

    def tearDown(self):
        Location.objects.all().delete()
    

    def test_instance(self):
        self.assertTrue(isinstance(self.park, Location))

    #save test
    def test_save_location(self):
        self.park.save_location()
        location=Location.objects.all()
        self.assertTrue(len(location) > 0)


    def test_delete_location(self):
        self.outside=Location(name="outside")
        self.outside.save_location()
        location=Location.objects.all()

        self.outside.delete_location()
        self.assertEqual(len(location), 0)

    def test_update_location(self):
        self.park.save_location()
        Location.objects.filter(name="park").update(name="cafe")
        self.assertTrue(Location.objects.get(name="cafe"))


class CategoryTestClass(TestCase):
    #setUpmethod

    def setUp(self):
        self.outside = Category(name="outside")

    def tearDown(self):
        Location.objects.all().delete()
    

    def test_instance(self):
        self.assertTrue(isinstance(self.outside, Category))

    #save test
    def test_save_category(self):
        self.outside.save_category()
        category=Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_category(self):
        self.outside=Category(name="wildlife")
        self.outside.save_category()
        category=Category.objects.all()

        self.outside.delete_category()
        self.assertEqual(len(category), 0)

    def test_update_category(self):
       self.outside.save_category()
       Category.objects.filter(name="outside").update(name="inside")
       self.assertTrue(Category.objects.get(name="inside"))
