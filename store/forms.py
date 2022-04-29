from .models import Comments
from django import forms



class CommentForm(forms.ModelForm):
    name = forms.CharField(label=False,widget=forms.TextInput(attrs={"class": "myfield", 'placeholder': 'Имя'}))
    tel = forms.CharField(label=False,widget=forms.TextInput(attrs={"class": "myfield1", 'placeholder': 'Телефон'}))
    body = forms.CharField(label=False,widget=forms.Textarea(attrs={"class": "myfield2", 'placeholder': 'Оставить отзыв...'}))
    class Meta:
        model = Comments
        fields = ('name', 'tel', 'body')