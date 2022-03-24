from django.test import TestCase
from .models import *
# Create your tests here.

class ProfileTestClass(TestCase):

    def setUp(self):
        self.ann = profile(name="Try",Location="Townie",occupation="Driver")

    def test_instance(self):
        self.assertTrue(isinstance(self.ann,profile))

    def tearDown(self):
        profile.objects.all().delete()

    def test_save_method(self):
        self.ann.save_profile()
        profile= Profile.objects.all()
        self.assertTrue(len(profile)>0)

    def test_delete_method(self):
        self.ann.delete_profile('Site')
        profile = Profile.objects.all()
        self.assertTrue(len(profile)==0)

class LocalsTestClass(TestCase):
    def setUp(self):
        self.ann = locals(name="Try",Location="Townie",email="services@gmail.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.ann,locals))

    def tearDown(self):
        locals.objects.all().delete()

    def test_save_method(self):
        self.ann.save_locals()
        locals= Locals.objects.all()
        self.assertTrue(len(locals)>0)

    def test_delete_method(self):
        self.ann.delete_locals('Site')
        locals = Locals.objects.all()
        self.assertTrue(len(locals)==0)
        