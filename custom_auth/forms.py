from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    run = forms.CharField(max_length=9, required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email','run')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.run = self.cleaned_data["run"]
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


