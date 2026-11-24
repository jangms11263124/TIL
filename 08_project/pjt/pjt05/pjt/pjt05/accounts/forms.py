from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    nickname = forms.CharField(
        required=True,
        label = '별명'
    )
    interest_stocks = forms.MultipleChoiceField(
        choices=[
            ('SAMSUNG', '삼성전자'),
            ('SKHYNIX', 'SK하이닉스'),
            ('NAVER', '네이버'),
            ('LGINNOTEK', 'LG이노텍'),
            ('HDCAR', '현대차'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label = "관심 종목",
    )

    profile_image = forms.ImageField(
        label = '프로필 이미지'
    )    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('nickname', 'profile_image', 'interest_stocks')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.interest_stocks = ",".join(self.cleaned_data.get('interest_stocks'))
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('nickname', 'profile_image', 'interest_stocks')
