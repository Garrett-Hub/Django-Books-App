from django.forms import ModelForm, Textarea
from .models import Author, Book


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'firstName': 'First Name',
            'lastName': 'Last Name',
        }


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'year': 'Year Published',
        }
        widgets = {
            'description': Textarea(attrs={'rows': 3, 'style': 'resize:none;'}),
        }
