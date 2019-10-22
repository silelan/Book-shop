from django import forms
from .models import *

class BookInfoForm(forms.ModelForm):
    class Meta:
        model = BookInfo
        fields = "__all__"

class BookSoldForm(forms.ModelForm):
    class Meta:
        model = BookSold
        fields = "__all__"