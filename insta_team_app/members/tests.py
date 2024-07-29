from django.test import TestCase, Client
from django.urls import reverse
from members.models import Member
from members.forms import MemberForm

class MemberFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'first_name': 'Akshay',
            'last_name': 'Narkhede',
            'emailId': 'akshay@example.com',
            'phone': '987-654-3210',
            'role': 'r'
        }
        form = MemberForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'first_name': '', 
            'last_name': 'Narkhede',
            'emailId': 'invalid-email',
            'phone': '123', 
            'role': 'r'
        }
        form = MemberForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)


class ModelViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('member_list')
        self.add_url = reverse('member_add')
        self.edit_url = reverse('member_edit', args=[1])  
        self.delete_url = reverse('member_delete', args=[1])
        self.member = Member.objects.create(
            first_name="Akshay",
            last_name="Narkhede",
            emailId="narkhede.aks@example.com",
            phone="123-456-7890",
            role="r"
        )

    def test_member_list_view(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Akshay Narkhede')

    def test_member_add_view(self):
        response = self.client.get(self.add_url)
        self.assertEqual(response.status_code, 200)

    def test_member_edit_view(self):
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Edit team member')