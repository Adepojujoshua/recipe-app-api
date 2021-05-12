from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating new user is successful"""
        email = 'adepojuayobami4real@gmail.com'
        password = 'testpwd123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password, password)

    def test_new_user_email_normalize(self):
        """Test the email for a new user is normalize"""
        email = 'test@NAIJADEV.com'
        user = get_user_model().objects.create_user(email, 'randomstr')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test if new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
