from pydoc_data.topics import topics

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from newspaper.forms import NewspaperForm, RedactorForm
from newspaper.models import Topic, Redactor


class NewspaperFormTest(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name='Test Topic')
        self.redactor = Redactor.objects.create(
            username="test_redactor",
            password="Test123",
            years_of_experience=0
        )

    def test_form_is_valid(self):
        form = NewspaperForm(data={
            'title': 'Test Newspaper',
            "content": "Test Content",
            "published_date": timezone.now(),
            "topics": [self.topic.id],
            "publishers": [self.redactor.id],
        })
        self.assertTrue(form.is_valid())


class RedactorFormTest(TestCase):
    def setUp(self):
        self.valid_data = {
            "username": "test_redactor",
            "password": "NotEasyPAss123!",
            "first_name": "Test",
            "last_name": "Test",
            "email": "test@gmail.com",
            "years_of_experience": 1
        }

    def create_form(self, **kwargs):
        data = self.valid_data.copy()
        data.update(kwargs)
        return RedactorForm(data=data)


    def test_form_is_valid_with_correct_data(self):
        form = self.create_form()
        self.assertTrue(form.is_valid())

    def test_form_is_valid_with_weak_data(self):
        form = self.create_form(password="testweakpassword")
        self.assertFalse(form.is_valid())

    def test_clean_password_raises_validation_error(self):
        form = self.create_form(password="weakpass")
        self.assertFalse(form.is_valid())
        self.assertIn("password", form.errors)
