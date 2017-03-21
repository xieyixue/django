from django.test import TestCase

# Create your tests here.
class AppOne(TestCase):

    def test_hello(self):
        rsp = self.client.get('/hello/')
        print rsp
