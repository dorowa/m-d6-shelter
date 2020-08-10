from django import forms
from pets.models import PetSpecie, Kind, Breed, Volunteer, PetAction
from django.utils.translation import gettext_lazy as _

class KindForm(forms.ModelForm):
    kind_name = forms.CharField(widget=forms.TextInput, label="Вид")
    kind_info = forms.CharField(widget=forms.TextInput, label="Краткое описание")
    class Meta:
        model = Kind
        fields = "__all__"

