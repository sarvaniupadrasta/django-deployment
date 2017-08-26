from django import forms
from AppTwo.models import User

class NewUserForm(forms.ModelForm):
    #fields

    class Meta():
        model = User
        fields = "__all__"
