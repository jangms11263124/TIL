from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

# def sample(self):
#   return 

class ArticleForm(forms.ModelForm):
    # Python의 Inner class라는 문법과 무관.
    class Meta:
        model = Article
        fields = '__all__'
                    # 튜플
        # exclude = ('title',)
        # include = ('title',)

    # def sample(self):
    #     return 

