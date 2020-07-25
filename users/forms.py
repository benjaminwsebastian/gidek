from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile  # , Report
from PIL import Image
from django.core.files import File
from io import BytesIO


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    agreed = forms.BooleanField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "agreed"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


DELETE_REASONS = (
    (
        "I am not getting enough value from my membership",
        "I am not getting enough value from my membership",
    ),
    (
        "Concerned about my data/ privacy concerns",
        "Concerned about my data/ privacy concerns",
    ),
    (
        "I don't understand how to use this service",
        "I don't understand how to use this service",
    ),
    ("This service is not working for me", "This service is not working for me"),
    ("My account was hacked", "My account was hacked"),
)


class UserDeleteForm(forms.Form):
    reason = forms.CharField(
        label="Why are you deleting your account?",
        widget=forms.Select(choices=DELETE_REASONS),
    )
    password = forms.CharField(
        widget=forms.PasswordInput, label="To continue, please re-enter your password"
    )

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(UserDeleteForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        valid = self.user.check_password(self.cleaned_data["password"])
        if not valid:
            raise forms.ValidationError("Password Incorrect")


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "address",
            "city",
            "country",
            "postal_code",
            "about",
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].required = False
        self.fields["last_name"].required = False
        self.fields["address"].required = False
        self.fields["city"].required = False
        self.fields["country"].required = False
        self.fields["postal_code"].required = False
        self.fields["about"].required = False


class ProfileImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]

    def save(self, commit=True):
        profile = super(ProfileImageUpdateForm, self).save(commit=False)

        img = Image.open(self.cleaned_data["image"])
        min_side = min(img.height, img.width)
        output_size = (min_side, min_side)
        img.thumbnail(output_size)

        blob = BytesIO()
        img.save(profile.image.path)
        profile.image = img

        profile.save()
        return profile
