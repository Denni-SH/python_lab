from django import forms
from .validator import validate_url
class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Enter url (with http(s)://)',validators=[validate_url])
