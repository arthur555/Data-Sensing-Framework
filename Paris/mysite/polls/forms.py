from django import forms
from .models import Post
class HomeForm(forms.ModelForm):
    post = forms.CharField()
    #cluster = forms.CharField()
    class Meta:
        model = Post
        fields = ('post',)
