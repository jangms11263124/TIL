from django.contrib.auth.forms import UserCreationForm
# from .models import User
from django.contrib.auth import get_user_model  

# 그냥 form이 아니라 model form 
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # model = User 
        model = get_user_model()
        # fields = 