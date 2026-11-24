from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '올바른 제목을 입력하세요.'}),
            'content': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': '자유롭게 의견을 남겨주세요.'}),
            'author': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '익명'}),
        }
