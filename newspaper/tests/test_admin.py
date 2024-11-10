from django.urls import reverse

from django.test import TestCase, Client
from django.contrib.auth import get_user_model


class AdminTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username='testuser',
            password='Test_admin',
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_user(
            username='redactor',
            password='testredactor',
            email='test@gmail.com',
            years_of_experience=2
        )


    def test_redactor_years_of_experience_lest(self):
        url = reverse("admin:newspaper_redactor_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)

    def test_redactor_detail_years_of_experience(self):
        url = reverse("admin:newspaper_redactor_change", args=[self.redactor.id])
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)

    def test_redactor_add_years_of_experience_lest(self):
        url = reverse("admin:newspaper_redactor_add")
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)