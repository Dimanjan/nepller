from urllib import response
from django.test import TestCase,Client
from TUsers.models import TUser

class TUserTestCase(TestCase):
    def setUp(self):
        TUser.objects.create(
            username="swornim_wagle",
            password="bestnepalieconomist",
            country="NP")

        def test_create(self):
            self.assertEqual("NP",
                      TUser.objects.get(username="swornim_wagle").country)

        def test_api_login(self):
            client=Client()
            response= client.post('/login/',{'username':'swornim_wagle'},format='json')
        self.assertEqual(200,response.status_code)