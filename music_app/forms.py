from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label="Search for a song", max_length=255)
