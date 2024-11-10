from django.contrib.auth import get_user_model
from django.test import TestCase

from newspaper.models import Topic, Newspaper, Redactor


class ModelTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(
            name='Test',
        )
        self.assertEqual(str(topic), f"{topic.name}")

    def test_newspaper_str(self):
        topic = Topic.objects.create(
            name='Test',
        )
        publisher = Redactor.objects.create(
            username='Test',
            years_of_experience=0
        )
        newspaper = Newspaper.objects.create(
            title='Test',
            content='Test',
            published_date="2020-01-01",
        )
        newspaper.topics.set([topic])
        newspaper.publishers.set([publisher])
        self.assertEqual(str(newspaper), f"{newspaper.title}")

    def test_redactor_str(self):
        username = 'Test'
        years_of_experience = 0
        password = 'Test123'
        redactor = get_user_model().objects.create_user(
            username=username,
            years_of_experience=years_of_experience,
            password=password
        )
        self.assertEqual(redactor.username, username)
        self.assertTrue(redactor.check_password(password))
        self.assertEqual(redactor.years_of_experience, years_of_experience)
