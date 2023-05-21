from .models import Profile, Image
from django.forms import ModelForm
from django import forms
from ckeditor.widgets import CKEditorWidget


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

class ImageForm(ModelForm):
    article = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Image
        fields = '__all__'
        #widgets = {
            #'profile': forms.TextInput(attrs={'type': 'hidden'})
        #}
        exclude = ['user']
