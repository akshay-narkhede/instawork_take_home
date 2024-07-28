from django import forms
from .models import Member
import re

class MemberForm(forms.ModelForm):
    phone = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'placeholder': 'xxx-xxx-xxxx'}))

    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'emailId', 'phone', 'role']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.strip():
            raise forms.ValidationError("First name cannot be blank.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.strip():
            raise forms.ValidationError("Last name cannot be blank.")
        return last_name

    def clean_emailId(self):
        email = self.cleaned_data.get('emailId')
        print("clean_emailId : ", email)
        # Check for existing email (exclude the current instance if updating)
        if Member.objects.filter(emailId=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("A member with this email already exists.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise forms.ValidationError("Enter a valid email address.")
        
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        phone = re.sub(r'\D', '', phone) 
        if len(phone) != 10:
            raise forms.ValidationError("Phone number must be 10 digits.")
        return f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"