from django.forms import ModelForm
from django import forms

from .models import *

class DateInputWidget(forms.DateInput):
    input_type = 'date'

class TimeInputWidget(forms.DateInput):
    input_type = 'time'

class playerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        exclude = ['modified_by']

        widgets = {
            'ingame_name': forms.TextInput(attrs={'class': 'form-control', 'autofocus': True, 'required': True}),
            'discord_name': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'steam_id': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': False}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'required': False, 'rows': '5'}),
            'squad': forms.Select(attrs={'class': 'form-control', 'required': False}),            
        }
   
    def save(self, user):
        obj = super().save(commit = False)
        obj.modified_by = user
        obj.save() 
        return obj

class squadForm(ModelForm):
    class Meta:
        model = Squad
        fields = '__all__'
        exclude = ['modified_by']

        widgets = {
            'squad_name': forms.TextInput(attrs={'class': 'form-control', 'autofocus': True, 'required': True}),
            'squad_leader': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'required': False, 'rows': '5'}),
        }

    def save(self, user):
        obj = super().save(commit = False)
        obj.modified_by = user
        obj.save() 
        return obj

class donationForm(ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'
        exclude = ['modified_by']

        help_texts = {'donation_date': "Eg. 31.12.2020 23:59:00",}

        widgets = {
            'amount': forms.TextInput(attrs={'autofocus': True, 'required': True}),            
            'note': forms.Textarea(attrs={'required': False, 'rows': '5'}),
            'donation_date' : forms.DateTimeInput(attrs={'placeholder': 'dd.mm.yyyy eg. 31.12.2001'}),
            'player': forms.Select(attrs={'required': False}),        
            }

    def save(self, user):
        obj = super().save(commit = False)
        obj.modified_by = user
        obj.save() 
        return obj

class vehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        exclude = ['modified_by']

        widgets = {
            'player': forms.Select(attrs={'class': 'form-control', 'required': False}), 
            'vehicle_id': forms.TextInput(attrs={'class': 'form-control', 'required': False}),           
            'vehicle_type': forms.Select(attrs={'class': 'form-control', 'required': False}),        
            'note': forms.Textarea(attrs={'class': 'form-control', 'required': False, 'rows': '5'}),
               }

    def save(self, user):
        obj = super().save(commit = False)
        obj.modified_by = user
        obj.save() 
        return obj

class caseForm(ModelForm):
    class Meta:
        model = Case
        fields = '__all__'
        exclude = ['modified_by']
        
        widgets = {
            'player': forms.Select(attrs={'autofocus': True, 'required': False}),
            'case_type': forms.Select(attrs={'required': True}),
            'case_date': forms.DateInput(attrs={'placeholder': '31.12.2020 23:59:59'}),
            'case_location': forms.TextInput(attrs={'required': False}),
            'note': forms.Textarea(attrs={'required': False, 'rows': '5'}),
            'is_active': forms.CheckboxInput(attrs={'disabled': False}),
            }

    def save(self, user):
        obj = super().save(commit = False)
        obj.modified_by = user
        obj.save() 
        return obj

class flagForm(ModelForm):
    class Meta:
        model = Flag
        fields = '__all__'
        exclude = ['modified_by']

        widgets = {
            'player': forms.Select(attrs={'autofocus': True, 'required': False}),
            'squad_leader': forms.TextInput(attrs={'required': False}),
            'note': forms.Textarea(attrs={'required': False, 'rows': '5'}),
        }

    def save(self, user):
        obj = super().save(commit = False)
        obj.modified_by = user
        obj.save() 
        return obj