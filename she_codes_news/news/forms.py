from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory 
        # Why does this need to be indented?* 
    fields = ['title', 'author', 'pub_date', 'content']