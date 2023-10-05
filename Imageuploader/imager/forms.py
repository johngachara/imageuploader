from django import forms
from .models import gachara

class PostForm(forms.ModelForm):
    class Meta:
        model = gachara
        fields = ['title','image']
