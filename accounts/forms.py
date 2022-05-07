from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django.urls import reverse_lazy
from accounts.tasks import send_registration_email

from accounts.models import Profile


class AccountRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "first_name", "last_name", "email")

    def save(self, *args, **kwargs):
        self._send_email()
        return super().save(*args, **kwargs)

    def _send_email(self):
        send_registration_email.delay(self.cleaned_data['email'])


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
