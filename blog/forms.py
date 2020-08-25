from django import forms
from . models import Comment

# comment form
class CommentForm(forms.ModelForm):
    userEmail = forms.EmailField(widget=forms.TextInput(attrs={
        'name': 'userEmail', 'class': 'input-field', 'placeholder': 'Your email address here...'
    }))
    content = forms.Textarea(attrs={
        'name': 'content', 'class': 'input-field', 'placeholder': 'Your email address here...'
    })

    class Meta:
        model = Comment
        fields = ['userEmail', 'content']