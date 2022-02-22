from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django.urls import reverse_lazy

from accounts.models import Profile


class AccountRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "first_name", "last_name", "email")


class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ("first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get('password')
        if password:
            password.help_text = password.help_text.replace(
                '../password/', kwargs.pop(reverse_lazy(
                    'accounts:change_password'), './password')
            )


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
