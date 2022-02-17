from dataclasses import field
from .models import Song, Review
from django.forms import ModelForm, TextInput, Textarea, ChoiceField

class SongForm(ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.

    class Meta:
        model = Song
        fields = '__all__'
        widgets = {
            # "author": TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'ИМЯ'
            #     }),
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название трэка'
                }),
            
            "lyrics": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст трэка'
                })
        }




class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

      