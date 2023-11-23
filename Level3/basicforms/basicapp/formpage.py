from django import forms
from django.core import validators


class FormName(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    vemail = forms.EmailField(label="Enter Email Again")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    def clean(self):
        data = super().clean()
        email = data['email']
        vmail = data['vemail']
        if email != vmail:
            raise forms.ValidationError("Email Doesn't Match")