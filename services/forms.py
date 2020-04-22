from django import forms

# A form to create a new server
class ServerForm(forms.Form):
    display_name = forms.CharField(label="Server name", max_length=100)

class EmptyForm(forms.Form):
    display_name = forms.CharField(widget = forms.HiddenInput(), required = False)
