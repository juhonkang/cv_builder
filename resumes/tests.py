from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import CV

class CVModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create_user(username='testuser', password='testpass')
        CV.objects.create(name='John Doe', email='johndoe@example.com', mobile='+19999999999', github='https://github.com/johndoe', linkedin='https://linkedin.com/in/johndoe', summary='Test summary', user=User.objects.get(id=1))

    def test_name_label(self):
        cv = CV.objects.get(id=1)
        field_label = cv._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_email_label(self):
        cv = CV.objects.get(id=1)
        field_label = cv._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

class CVViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.cv_data = {'name': 'John Doe', 'email': 'johndoe@example.com', 'mobile': '+19999999999', 'github': 'https://github.com/johndoe', 'linkedin': 'https://linkedin.com/in/johndoe', 'summary': 'Test summary', 'user': self.user.id}

    def test_create_cv(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/cv/', self.cv_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_cv(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/cv/1/')
        self.assertEqual(response.status_code, 200)

    def test_update_cv(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put('/api/cv/1/', self.cv_data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_cv(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete('/api/cv/1/')
        self.assertEqual(response.status_code, 204)
