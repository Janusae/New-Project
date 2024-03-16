from django import forms
from .models import  Comment


class Comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ["date"]