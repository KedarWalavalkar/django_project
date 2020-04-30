from django import forms
from itvedantapp1.models import Users,Products,Category

class userform(forms.ModelForm):
    # disabled_fields = ('email',)
    class Meta:
        model=Users
        fields='__all__'
    # def __init__(self, *args, **kwargs):
    #     super(userform, self).__init__(*args, **kwargs)
    #     for field in self.disabled_fields:
    #         self.fields[field].disabled = True

class productform(forms.ModelForm):
    class Meta:
        model=Products
        fields='__all__'

class categoryform(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'
