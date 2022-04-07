from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from application.models import Category


class RegistrationUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def clean_name(self):
        data = self.cleaned_data['name']

        if len(data) < 5:
            raise ValidationError("Длина должна быть больше 5!")
        if len(data) > 25:
            raise ValidationError("Длина должна быть не больше 25!")
        return data
