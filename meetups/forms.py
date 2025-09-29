from django import forms

from .models import Participant

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email')

# Outro jeito de fazer a mesma coisa
# class RegistrationForm(forms.ModelForm):
#    class Meta:
#        model = Participant
#        fields = ['email']
