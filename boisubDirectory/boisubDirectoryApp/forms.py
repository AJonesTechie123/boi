from django.forms import ModelForm, TextInput
from .models import Books

class BookForm(ModelForm):
     class Meta:
        model = Books
        fields = ['title', 'author_first_name', 'author_last_name']
        widgets = {
            'title': TextInput(attrs={'class' : 'input', 'placeholder' : 'Book Name'}),
        } 
