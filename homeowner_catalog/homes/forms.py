

from django import forms

from homeowner_catalog.domain.models import Home


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        exclude = ['owner', 'agents', 'assistants']
