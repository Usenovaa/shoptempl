from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

UserClass = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        UserClass = get_user_model()
        UserClass.objects.create(
            username='username',
            email='email@fgg',
            password='password'
        )

    def test_check(self):
        UserClass = get_user_model()
        user = UserClass.objects.get(
            username='username',
        )
        self.assertTrue(len(user.email.split('@')) > 1)

