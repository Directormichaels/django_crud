from django import forms
from .models import Post

class PostForm(forms):
    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "author",
            "body",
            "publish",
            "created",
            "updated",
            "status"
        ]