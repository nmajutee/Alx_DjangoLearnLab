from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Book


class BookForm(forms.ModelForm):
    """
    Form for creating and editing Book instances.
    """

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book title',
                'maxlength': 200,
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter author name',
                'maxlength': 100,
            }),
            'publication_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter publication year',
                'min': 1000,
                'max': 2030,
            }),
        }
        labels = {
            'title': _('Book Title'),
            'author': _('Author Name'),
            'publication_year': _('Publication Year'),
        }
        help_texts = {
            'title': _('The title of the book'),
            'author': _('The author(s) of the book'),
            'publication_year': _('The year this book was published'),
        }

    def clean_publication_year(self):
        """
        Validate the publication year to ensure it's reasonable.
        """
        year = self.cleaned_data.get('publication_year')
        if year:
            import datetime
            current_year = datetime.datetime.now().year
            if year > current_year:
                raise forms.ValidationError(
                    _('Publication year cannot be in the future.')
                )
            if year < 1000:
                raise forms.ValidationError(
                    _('Publication year must be at least 1000.')
                )
        return year

    def clean_title(self):
        """
        Validate the title to ensure it's not empty or just whitespace.
        """
        title = self.cleaned_data.get('title')
        if title:
            title = title.strip()
            if not title:
                raise forms.ValidationError(_('Title cannot be empty.'))
        return title

    def clean_author(self):
        """
        Validate the author to ensure it's not empty or just whitespace.
        """
        author = self.cleaned_data.get('author')
        if author:
            author = author.strip()
            if not author:
                raise forms.ValidationError(_('Author cannot be empty.'))
        return author