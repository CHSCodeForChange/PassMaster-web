from django import forms
from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from accounts.models import *
from server.models import *


class EditPasswordForm(PasswordChangeForm):
    template_name = '/accounts/edit_password'

    old_password = forms.CharField(label= 'Old Password', required=False, widget=forms.PasswordInput(
        attrs={'type': 'text',
               'class': 'form-control'}
    ))
    new_password1 = forms.CharField(label='New Password', required=False, widget=forms.PasswordInput(
        attrs={'type': 'text',
               'class': 'form-control'}
    ))
    new_password2 = forms.CharField(label='Confirm New Password', required=False, widget=forms.PasswordInput(
        attrs={'type': 'text',
               'class': 'form-control'}
    ))

    def clean(self):

        data= self.cleaned_data

        if data.get('old_password') and data.get('new_password1') and data.get('new_password2'):
            pass
        else:
            raise forms.ValidationError('Some Fields Missing')

        return data



# The form for user signups
class SignupForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=150, widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control form',
               'placeholder': 'First Name'}))

    last_name = forms.CharField(label='Last Name', max_length=150, widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control form',
               'placeholder': 'Last Name'}))
    username = forms.CharField(label='Username', min_length=4, max_length=150, widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control form',
               'placeholder': 'Username'}))
    email = forms.EmailField(label='Email', max_length=200, widget=forms.EmailInput(
        attrs={'type': 'text',
               'class': 'form-control form',
               'placeholder': 'Email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'type': 'password',
               'class': 'form-control form',
               'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'type': 'password',
               'class': 'form-control form',
               'placeholder': 'Confirm Password'}))

    member_type = forms.ChoiceField(choices=Profile.CHOICES, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control form',
               'placeholder': 'Role'}))


    # May only contain alphabetical characters
    def clean_firstname(self):
        first_name = self.cleaned_data['first_name'].title()
        if not first_name.isalpha():
            raise ValidationError("Your name must contain only letters")
        return first_name

    # May only contain alphabetical characters
    def clean_lastname(self):
        last_name = self.cleaned_data['last_name'].title()
        if not last_name.isalpha():
            raise ValidationError("Your name must contain only letters")
        return last_name

    # Must be unique
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    # Must be unique
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    # Used for validation
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        # Passwords must be 16+ characters long or contain a digit
        if len(password1) < 16 and not any(char.isdigit() for char in password1):
            raise ValidationError("Your password must either be 16+ letters long or contain a digit.")

        return password2

    def clean_member_type(self):
        return self.cleaned_data['member_type']

    # Save a new user and set their Group to Volunteer
    def save(self):
        try:
            user = User.objects.create_user(
                self.cleaned_data['username'],
                self.cleaned_data['email'],
                self.cleaned_data['password1'],
            )
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.is_active = True

            member_type = self.cleaned_data['member_type']

            user.save()

            profile = Profile(user=user, member_type=member_type)
            profile.save()

            if profile.is_student():
                student = Student(profile=profile)
                student.save()
            elif profile.is_teacher():
                teacher = Teacher(profile=profile)
                teacher.save()
            elif profile.is_administrator():
                admin = Administrator(profile=profile)
                admin.save()
            elif profile.is_location():
                location = Location(profile=profile)
                location.save()

            return user


        except Exception as e:
            raise


class LoginForm(AuthenticationForm):
  username = UsernameField(
    max_length=254,
    widget=forms.TextInput(
      attrs={'autofocus': True,
             'type': 'text',
             'class': 'form-control'
             }),
  )
  password = forms.CharField(
    label=_("Test"),
    strip=False,
    widget=forms.PasswordInput(
      attrs={'type': 'text',
             'class': 'form-control'}
    ),
  )

  def __init__(self, request):
    AuthenticationForm.__init__(self, request)
