from django import forms
from blog.models import Comment



class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['post','name','email','subject','message']