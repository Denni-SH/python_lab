from django import forms
from .models import Book,Author,Category


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ('title',)

class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = ('name','born_year',)

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('title','year','description','authors','category',)
