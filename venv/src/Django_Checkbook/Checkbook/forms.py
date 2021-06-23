# this file was created by the dev

from django.forms import ModelForm
from .models import Account, Transaction

class AccountForm(ModelForm):
    class Meta:
        model = Account
        # instead of writing out all of the fields from Account on the models.py doc use __all__
        # grab all the fields within our Account class
        # pass into the form
        fields = '__all__'

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        # instead of writing out all of the fields from Transaction on the models.py doc use __all__
        # grab all the fields within our Transaction class
        # pass into the form
        fields = '__all__'

