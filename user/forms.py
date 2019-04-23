from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'subscription')
        field_classes = {'username': UsernameField}
