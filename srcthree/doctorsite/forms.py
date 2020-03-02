from django import forms


class PatientForm(forms.Form):
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    age1 = forms.IntegerField(min_value=0, max_value=99)
    number= forms.IntegerField(min_value=0)


class SendEmailForm(forms.Form):
    receiver = forms.EmailField()




