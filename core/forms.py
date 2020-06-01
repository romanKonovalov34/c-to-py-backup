import datetime

from django import forms
from django.core.exceptions import ValidationError


from .models import User
#from .models import Doctor
from .models import Patient
from .models import Ancket
from .models import Question
from .models import Disease
from .models import Epicriz

class SigninForm(forms.Form):
    login = forms.CharField(max_length=50, label="login")
    password = forms.CharField(max_length=50, label="password", widget=forms.PasswordInput())
    isAdmin = forms.BooleanField(required=False, label='i am admin')

    login.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    isAdmin.widget.attrs.update({'class': 'form-control'})



class RegisterForm(forms.Form):
    login = forms.CharField(max_length=50, label="login")
    password = forms.CharField(max_length=50, label="password", widget=forms.PasswordInput())
    rePassword = forms.CharField(max_length=50, label="repeat password", widget=forms.PasswordInput())
    
    login.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    rePassword.widget.attrs.update({'class': 'form-control'})

    

class DbPatientsForm(forms.Form):
    number_card = forms.CharField(required='', max_length=50, label="number card")
    FIO = forms.CharField(required='', max_length=100, label="First last middle name")
    date_birth = forms.CharField(required='', label='birthday', widget=forms.TextInput(attrs={'placeholder': 'Please use the following format: DD.MM.YYYY'}))
    sex = forms.CharField(required='', max_length=50, label="sex")
    nationality = forms.CharField(required='', max_length=50, label="nationality")
    education = forms.CharField(required='', max_length=100, label="education")
    address = forms.CharField(required='', max_length=100, label="adress")
    phone = forms.CharField(required='', max_length=50, label="phons")
    job = forms.CharField(required='', max_length=100, label="where work")
    position = forms.CharField(required='', max_length=100, label="position")

    number_card.widget.attrs.update({'class': 'form-control'})
    FIO.widget.attrs.update({'class': 'form-control'})
    date_birth.widget.attrs.update({'class': 'form-control'})
    sex.widget.attrs.update({'class': 'form-control'})
    nationality.widget.attrs.update({'class': 'form-control'})
    education.widget.attrs.update({'class': 'form-control'})
    address.widget.attrs.update({'class': 'form-control'})
    phone.widget.attrs.update({'class': 'form-control'})
    job.widget.attrs.update({'class': 'form-control'})
    position.widget.attrs.update({'class': 'form-control'})

    
class DbQuestionsForm(forms.Form):
    question_id = forms.IntegerField(required='', label="id")
    question = forms.CharField(required='', max_length=100, label="First last middle name")

    question_id.widget.attrs.update({'class': 'form-control'})
    question.widget.attrs.update({'class': 'form-control'})

class DbDiseasesForm(forms.Form):
    diseases_id = forms.IntegerField(required='', label="id")
    name = forms.CharField(required='', max_length=100, label="name")
    note = forms.CharField(required='', label="note")

    diseases_id.widget.attrs.update({'class': 'form-control'})
    name.widget.attrs.update({'class': 'form-control'})
    note.widget.attrs.update({'class': 'form-control'})

# анкета
class DBAncketsForm(forms.Form):
    number_card = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    number_ancket = forms.CharField(required='', label="card")
    question = forms.ModelChoiceField (queryset = Question.objects.all(),to_field_name="question")
    answer = forms.CharField(required='', label="answer")
    conviction = forms.IntegerField(required='', label="conviction")

    number_card.widget.attrs.update({'class': 'form-control'})
    number_ancket.widget.attrs.update({'class': 'form-control'})
    question.widget.attrs.update({'class': 'form-control'})
    answer.widget.attrs.update({'class': 'form-control'})
    conviction.widget.attrs.update({'class': 'form-control'})
    
class PostuplenieForm(forms.Form):
    number_card = forms.IntegerField(label="number card")

    number_card.widget.attrs.update({'class': 'form-control'})


class ProfileForm(forms.Form):
    FIO = forms.CharField(required='', label="First last middle name doctor")
    login = forms.CharField(required='', label="login")
    postion = forms.CharField(required='', label="position")
    department = forms.CharField(required='', label="department")
    password = forms.CharField(label="login", widget=forms.PasswordInput())

    FIO.widget.attrs.update({'class': 'form-control'})
    login.widget.attrs.update({'class': 'form-control'})
    postion.widget.attrs.update({'class': 'form-control'})
    department.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    
class DBEpicrizForm(forms.Form):
    number_card = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    number_epic = forms.CharField(required='')
    invalid = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    lechenie = forms.CharField(required='', label='lechenie')
    date_gospit = forms.CharField(required='', label='date hospital', widget=forms.TextInput(attrs={'placeholder': 'Please use the following format: YYYY-MM-DD'}))
    date_vipisky = forms.CharField(required='', label='date out', widget=forms.TextInput(attrs={'placeholder': 'Please use the following format: YYYY-MM-DD'}))

    number_card.widget.attrs.update({'class': 'form-control'})
    number_epic.widget.attrs.update({'class': 'form-control'})
    invalid.widget.attrs.update({'class': 'form-control'})
    lechenie.widget.attrs.update({'class': 'form-control'})
    date_gospit.widget.attrs.update({'class': 'form-control'})
    date_vipisky.widget.attrs.update({'class': 'form-control'})

class DbDiagnosesForm(forms.Form):
    number_card = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}), label="card")
    number_diag = forms.CharField(required='', label="id diagnoses")
    note = forms.CharField(required='', max_length=100, label="diagnoses note")
    disease = forms.ModelChoiceField (queryset = Disease.objects.all(), to_field_name="name", label="disease")
    epicriz = forms.ModelChoiceField (queryset = Epicriz.objects.all(), to_field_name="lechenie", label="epicris")

    number_card.widget.attrs.update({'class': 'form-control'})
    number_diag.widget.attrs.update({'class': 'form-control'})
    note.widget.attrs.update({'class': 'form-control'})
    disease.widget.attrs.update({'class': 'form-control'})
    epicriz.widget.attrs.update({'class': 'form-control'})
