from django import forms
from komment.models import Comment


class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'text')
