from django import forms
from captcha.fields import CaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label='Your Email')
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}), required=False, label='Phone Number')
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False,
                                 label='Attachments (multiple is allowed)')
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                'from_email',
                'subject',
                'message',
                'phone',
                Field('file_field', css_class="")
            )
        )
        super(ContactForm, self).__init__(*args, **kwargs)
