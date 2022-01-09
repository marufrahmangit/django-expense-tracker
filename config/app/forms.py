from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit
from django import forms
from .models import Expenditure,Item,Bank


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expenditure
        fields = ('item', 'date', 'amount', 'remarks')
        widgets = {
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name',)


class BankForm(forms.ModelForm):

    class Meta:
        model = Bank
        fields = ('opening_bal',)
