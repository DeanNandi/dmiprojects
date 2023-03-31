from django import forms
from .models import Projects, Inkind, Cash, Purchases, Brought, Dispensing
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class MyForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['name', 'country', 'email', 'date_of_creation']
        labels = {'name': 'Name of Program', 'country': 'Country Based', 'email': 'Email Address',
                  'date_of_creation': 'Date Today' }


class Inkind_form(forms.ModelForm):
    class Meta:
        model = Inkind
        fields = ['item_name', 'organization', 'program_name', 'quantity', 'date_supplied']
        labels = {'item_name': 'Name of item', 'organization': 'Who Donated',  'program_name':'Program Name', 'quantity': 'Quantity',
                  'date_supplied': 'Date Supplied' }


class cash_form(forms.ModelForm):
    class Meta:
        model = Cash
        fields = ['amount_received', 'organization', 'program_name', 'date_issued']
        labels = {'amount_received': 'Amount Received', 'organization': 'Who Donated', 'program_name':'Program Name',
                  'date_issued': 'Date Issued'}


class purchases_form(forms.ModelForm):
    class Meta:
        model = Purchases
        fields = ['item_bought', 'item_price','program_name', 'quantity', 'date_bought']
        labels = {'item_bought': 'Item Bought', 'item_price': 'Price of Item','program_name':'Program Name',
                  'quantity': 'Quantity', 'date_bought': 'Date Bought'}


class Brought_form(forms.ModelForm):
    class Meta:
        model = Brought
        fields = ['item_brought', 'item_brand', 'organization','program_name', 'quantity', 'date_brought']
        labels = {'item_brought': 'Name of item', 'item_brand': 'Item Brand', 'organization': 'Who supplied',
                   'program_name':'Program Name','quantity': 'Quantity','date_brought': 'Date Supplied' }


class Dispensing_form(forms.ModelForm):
    class Meta:
        model = Dispensing
        fields = ['item_name', 'item_brand', 'organization','program_name', 'quantity', 'date_dispensed']
        labels = {'item_name': 'Name of item', 'item_brand': 'Item Brand', 'organization': 'Recipient',
                  'program_name':'Program That Dispensed','quantity': 'Quantity','date_dispensed': 'Date Supplied' }