from django import forms
from basicformsapp.models import User

# class FormName(forms.Form):
#
#     name = forms.CharField(label='Your name', max_length=100)
#     email = forms.EmailField(label='Your email', max_length=100)
#     text = forms.CharField(label="Type your Text Here",widget = forms.Textarea)

class NewUserForm(forms.ModelForm):
    class Meta:

        model = User
        fields = "__all__"

    # name = forms.CharField(label='Your name', max_length=100)
    # email = forms.EmailField(label='Your email', max_length=100)
    # text = forms.CharField(label="Type your Text Here",widget = forms.Textarea)


    # def __str__(self):
        # return(self.name, self.email,self.text)
