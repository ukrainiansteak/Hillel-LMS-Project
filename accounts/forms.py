from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy


class AccountRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "first_name", "last_name", "email")


class AccountProfileForm(UserChangeForm):
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

