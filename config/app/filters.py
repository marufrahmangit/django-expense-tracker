import django_filters
from django import forms
from .models import Expenditure


MONTH_CHOICES = [
    ('1','January'),('2','February'),('3','March'),('4','April'),('5','May'),('6','June'),
    ('7','July'),('8','August'),('9','September'),('10','October'),('11','November'),('12','December'),
]

YEAR_CHOICES = [
    ('2021','2021'),('2022','2022'),('2023','2023'),('2024','2024'),('2025','2025'),
]

class ExpenditureFilter(django_filters.FilterSet):
    month = django_filters.ChoiceFilter(field_name='date',label='Month',choices=MONTH_CHOICES,widget=forms.Select(attrs={'class':'form-control'}),lookup_expr='month')
    year = django_filters.ChoiceFilter(field_name='date',label='Year',choices=YEAR_CHOICES,widget=forms.Select(attrs={'class':'form-control'}),lookup_expr='year')

    class Meta:
        model = Expenditure
        fields = ('year','month')