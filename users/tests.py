from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from users.models import User
from users.serializers import UserSerializer

# tests for views

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(email= "",password="",first_name="", last_name=""):
        if first_name != "" and last_name != "" and email != "" and password != "":
            User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email = email,
                password = password
            )

    def setUp(self):
        '''
        add test data
        '''
        self.create_user("test@gmail.com", "test@123","hello","hello")
        self.create_user("test2@gmail.com", "test2@123","hello2","hello2")


class UpdateSongTest(BaseViewTest):

    def test_update_user(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("songs-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = User.objects.all()
        serialized = UserSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)