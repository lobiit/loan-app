from django import forms
from core.models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['loan_amount', 'number_of_years', 'interest_rate']
