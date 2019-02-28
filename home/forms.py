from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label='Your Email')
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}), required=False, label='Phone Number')
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False,
                                 label='Attachments (multiple is allowed)')
    captcha = CaptchaField()
