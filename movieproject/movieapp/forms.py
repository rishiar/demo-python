from django import  forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        field=['name','desc','year','img']