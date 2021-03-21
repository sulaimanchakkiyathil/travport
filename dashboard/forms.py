from django import forms

from dashboard.models import cust_registration_table


class cust_registration_form(forms.ModelForm):
    class Meta:
        model=cust_registration_table
        fields='__all__'

