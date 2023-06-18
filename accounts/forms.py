from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput,
        error_messages={
            'required': 'Введите пароль',
            'password_mismatch': 'Пароли не совпадают',
            'min_length': 'Пароль должен содержать не менее 8 символов',
            'numeric': 'Пароль не может быть полностью числовым',
            'common_password': 'Пароль не может быть общеупотребляемым',
            'similar_user_info': 'Пароль не может быть слишком похожим на вашу персональную информацию',
        }
    )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture', 'full_name', 'address']
