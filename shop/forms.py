from django import forms
from .models import Order
from .bulma_mixin import BulmaMixin
from .models import Review, RATE_CHOICES


class OrderForm(forms.Form, BulmaMixin):
    address = forms.CharField(label='Write your address')
    phone = forms.CharField(label='Write your phone')

    class Meta:
        model = Order
        fields = ['address', 'phone']


class RateForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), label='Write review text')
    rate = forms.ChoiceField(choices=RATE_CHOICES, required=True, label='Rate product from 1 to 5')

    class Meta:
        model = Review
        fields = ['text', 'rate']
