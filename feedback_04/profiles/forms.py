from django import forms


class ProfileForm(forms.Form):
  user_image = forms.ImageField(label='Your Image')