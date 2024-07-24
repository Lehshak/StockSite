from django import forms
from django.contrib.auth.models import User
from .models import Stock

class SearchForm(forms.Form):
    search_text = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Search'}), required=False)
    
class GrowthEstimationForm(forms.Form):
    stock_symbol = forms.ModelChoiceField(
        queryset=Stock.objects.all(),
        to_field_name="ticker",
        label="Select Stock Symbol"
    )
    years = forms.DecimalField(
        max_digits=5,
        decimal_places=1,
        min_value=0,
        label="Number of Years"
    )