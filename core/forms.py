import datetime

from django import forms
from django.core.exceptions import ValidationError

from .models import *
from django.db.models import Q

class CategoryForm(forms.Form):
    idCategory = forms.ModelChoiceField(queryset=Category.objects.all(), to_field_name="id", label="Категория")
    idGenus = forms.ModelChoiceField(queryset=Genus.objects.all(), to_field_name="id", label="Род")

    idCategory.widget.attrs.update({'class': 'form-control'})
    idGenus.widget.attrs.update({'class': 'form-control'})

class SignForm(forms.Form):
    login = forms.CharField(max_length=50, label="login")
    password = forms.CharField(max_length=50, label="password", widget=forms.PasswordInput())

    login.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})

class RegisterForm(forms.Form):
    login = forms.CharField(max_length=50, label="login")
    password = forms.CharField(max_length=50, label="password", widget=forms.PasswordInput())
    rePassword = forms.CharField(max_length=50, label="repeat password", widget=forms.PasswordInput())

    login.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    rePassword.widget.attrs.update({'class': 'form-control'})


class ProtocolForm(forms.Form):
    date = forms.DateField(initial=date.today(), label="Дата")
    address = forms.CharField(max_length=50, label="Адрес")
    coordinates = forms.CharField(required=False, max_length=50, label="Координаты")
    description = forms.CharField(required=False, max_length=1000, label="Описание", widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))

    date.widget.attrs.update({'class': 'form-control'})
    address.widget.attrs.update({'class': 'form-control'})
    coordinates.widget.attrs.update({'class': 'form-control'})
    description.widget.attrs.update({'class': 'form-control'})


class PersonForm(forms.Form):
    login = forms.CharField(max_length=50, label="Имя")
    email = forms.CharField(max_length=50, label="Почта")
    password = forms.CharField(max_length=50, label="Пароль")
    rePassword = forms.CharField(max_length=50, label="Пароль (подтверждение)")

    login.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    rePassword.widget.attrs.update({'class': 'form-control'})
    

class ChoiceGenus(forms.Form):
    idGenus = forms.ModelChoiceField(queryset=Genus.objects.all(), to_field_name="id", label="Вид")
    idGenus.widget.attrs.update({'class': 'form-control'})


class ProtocolFormChange(forms.Form):
    date = forms.DateField(initial=date.today(), label="Дата")
    address = forms.CharField(max_length=50, label="Адрес")
    coordinates = forms.CharField(required=False, max_length=50, label="Координаты")
    description = forms.CharField(required=False, max_length=1000, label="Описание", widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))
    report = forms.CharField(required=False, max_length=1000, label="Отчет", widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))
    
    date.widget.attrs.update({'class': 'form-control'})
    address.widget.attrs.update({'class': 'form-control'})
    coordinates.widget.attrs.update({'class': 'form-control'})
    description.widget.attrs.update({'class': 'form-control'})

class ChoiceThreatExemplar(forms.Form):
    idThreatExemplar = forms.ModelChoiceField(queryset=ThreatExemplar.objects.all(), to_field_name="id", label="Экземпляр")
    idThreatExemplar.widget.attrs.update({'class': 'form-control'})

