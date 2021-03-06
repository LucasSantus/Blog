from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'text')
        
        error_messages = {
            "title":{
                "required": "Title is required to complete the post.",
            },
            "text":{
                "required": "It is mandatory to fill in the text to complete the post."
            },
        }