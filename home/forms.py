from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}))
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
