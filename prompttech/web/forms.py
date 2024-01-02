from django import forms

from .models import Contact, JobApplication, Enquiry


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-gray', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'input-gray', 'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'class': 'input-gray', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'input-gray pt-4 form-control', 'placeholder': 'Message', 'rows': '5'}),
        }


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'phone', 'cv']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-gray', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'input-gray', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'input-gray', 'placeholder': 'Phone'}),
            'cv': forms.FileInput(attrs={'class': 'input-gray', 'placeholder': 'CV'}),
        }


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'contact', 'email', 'details']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-gray', 'placeholder': 'Name'}),
            'contact': forms.NumberInput(attrs={'class': 'input-gray', 'placeholder': 'Contact'}),
            'email': forms.EmailInput(attrs={'class': 'input-gray', 'placeholder': 'Email'}),
            'details': forms.Textarea(attrs={'class': 'input-gray pt-4 form-control', 'placeholder': 'Project Details', 'rows': '5'}),
        }