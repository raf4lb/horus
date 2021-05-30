from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Contact


class ContactTestCase(TestCase):

    def setUp(self):
        """
        Setup for the tests
        """
        # Create a user
        username = 'horus'
        password = 'horus12345678'
        self.user = User.objects.create_user(
            username=username, password=password
        )

        # User authentication
        self.client = APIClient()
        self.client.login(username=username, password=password)

    def test_create_contact(self):
        """
        Test if a user can create a contact.
        """
        data = {
            'owner': self.user.pk,
            'name': 'Rafael Albuquerque',
            'telephone': '88999034444',
        }
        url = reverse('contact-list')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.first().telephone, '88999034444')

    def test_update_contact_name(self):
        """
        Test if a user can update the contact name
        """
        # Create a contact for the user
        contact = Contact.objects.create(
            owner=self.user,
            name='Rafael Albuquerque',
            telephone='88999034444',
        )

        # Update the contact
        new_name = 'rafael Albuquerque'
        data = {
            'owner': self.user.pk,
            'name': new_name,
            'telephone': '88999034444',
        }
        url = reverse('contact-detail', args=[contact.pk])
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.get(
            pk=contact.pk).name, new_name
        )

    def test_update_contact_telephone(self):
        """
        Test if a user can update a contact.
        """
        # Create a contact for the user
        contact = Contact.objects.create(
            owner=self.user,
            name='Rafael Albuquerque',
            telephone='88999034444',
        )

        # Update the contact
        new_telephone = '88999034443'
        data = {
            'owner': self.user.pk,
            'name': 'Rafael Albuquerque',
            'telephone': new_telephone,
        }
        url = reverse('contact-detail', args=[contact.pk])
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.get(
            pk=contact.pk).telephone, new_telephone
        )

    def test_delete_contact(self):
        """
        Test if a user can delete a contact.
        """
        # Create a contact for the user
        contact = Contact.objects.create(
            owner=self.user,
            name='Rafael Albuquerque',
            telephone='88999034444',
        )
        url = reverse('contact-detail', args=[contact.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(
            Contact.objects.filter(pk=contact.pk, deleted=True).exists(),
            True,
        )
