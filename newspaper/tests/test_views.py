from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from newspaper.models import Topic, Newspaper, Redactor

TOPIC_URL = reverse('newspaper:topic-list')
NEWSPAPER_URL = reverse('newspaper:newspaper-list')
REDACTOR_URL = reverse('newspaper:redactor-list')


class PublicAccessTest(TestCase):
    def test_login_required_for_protected_pages(self):

        protected_urls = [
            TOPIC_URL,
            NEWSPAPER_URL,
            REDACTOR_URL,
        ]
        for url in protected_urls:
            with self.subTest(url=url):
                res = self.client.get(url)
                self.assertNotEqual(res.status_code, 200)


class PrivateAccessTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='Test123',
        )
        self.client.force_login(self.user)

    def test_retrieve_topics(self):
        Topic.objects.create(name="test topic")
        Topic.objects.create(name="test topic1")
        response = self.client.get(TOPIC_URL)
        self.assertEqual(response.status_code, 200)
        topics = Topic.objects.all()
        self.assertEqual(
            list(response.context["topic_list"]),
            list(topics),
        )
        self.assertTemplateUsed(response, "newspaper/topic_list.html")

    def test_retrieve_newspaper(self):
        topic = Topic.objects.create(name="test topic")
        newspaper = Newspaper.objects.create(
            title="test topic",
            content="test content",
            published_date="2020-01-01",
        )
        newspaper.topics.add(topic)

        response = self.client.get(NEWSPAPER_URL)
        self.assertContains(response, newspaper.title)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["newspaper_list"]),
            list(Newspaper.objects.all()),
        )
        self.assertTemplateUsed(response, "newspaper/newspaper_list.html")

    def test_retrieve_redactor(self):
        redactor = Redactor.objects.create(
            username="test1user",
            password="test123",
            years_of_experience=0
        )
        response = self.client.get(REDACTOR_URL)
        self.assertEqual(response.status_code, 200)
        redactors = Redactor.objects.all()
        self.assertIn(redactor, redactors)

        self.assertEqual(
            list(response.context["redactor_list"]),
            list(redactors),
        )
        self.assertTemplateUsed(response, "newspaper/redactor_list.html")
