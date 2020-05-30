from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@gmail.com', password='testpass'):
    """membuat sample user"""
    return get_user_model().objects.create_user(email, password)


class modelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Melalui test akan dibuat user dengan email bila sukses"""
        email = 'test@gmail.com'
        password = 'testpassword123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email untuk user baru yang di normalized"""
        email = 'test@GMAIL>COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test membuat user baru tanpa email akan error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test membuat superuser baru"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """test tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test tag string ingredient"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Tes recipe string"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Nasi Goreng',
            time_minutes=5,
            price=3.00
        )

        self.assertEqual(str(recipe), recipe.title)
