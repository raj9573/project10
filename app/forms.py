

# 1)Regex validators
# 2)Max value validator 
# 3)Minvalue validator 
# 4)Minlength validator
# 5)Maxlength validator
# 6)validate_email
# 7)validate_url


from django import forms 


from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['name']
        # exclude = ['age']


