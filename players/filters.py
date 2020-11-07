import django_filters
from django_filters import DateFilter, CharFilter
from django import forms

from .models import *

class PlayerFilter(django_filters.FilterSet):

    ingame_name = CharFilter(field_name='ingame_name', lookup_expr='icontains', label='Game name')
    discord_name = CharFilter(field_name='discord_name', lookup_expr='icontains', label='Discord name')
    class Meta:
        model = Player
        fields = '__all__'
        exclude = ['note','email','created','modified' ]

class SquadFilter(django_filters.FilterSet):

    ingame_name = CharFilter(field_name='ingame_name', lookup_expr='icontains', label='Game name')
    discord_name = CharFilter(field_name='discord_name', lookup_expr='icontains', label='Discord name')
    class Meta:
        model = Squad
        fields = '__all__'
        exclude = ['note','created','modified']


class DonationFilter(django_filters.FilterSet):
    donation_date = django_filters.DateTimeFilter(
        label='Donation Date',
        widget=forms.DateInput(attrs={'placeholder': '31.12.2020'}))

    o = django_filters.OrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('amount', 'amount'),
            ('donation_date', 'donation_date'),
        ),
        # labels do not need to retain order
        field_labels={
            'donation_date': 'Donation Date',
        }
    )
    #ingame_name = CharFilter(field_name='ingame_name', lookup_expr='icontains')
    #discord_name = CharFilter(field_name='discord_name', lookup_expr='icontains', label='Discord name')
    class Meta:
        model = Donation
        fields = '__all__'
        exclude = ['note','created','modified']


class VehicleFilter(django_filters.FilterSet):

    #ingame_name = CharFilter(field_name='ingame_name', lookup_expr='icontains')
    #discord_name = CharFilter(field_name='discord_name', lookup_expr='icontains', label='Discord name')
    class Meta:
        model = Vehicle
        fields = '__all__'
        exclude = ['note','created','modified']




class CaseFilter(django_filters.FilterSet):
    case_date = django_filters.DateTimeFilter(
        label='Case Date',
        widget=forms.DateInput(attrs={'placeholder': '31.12.2020'}))

    class Meta:
        model = Case
        fields = '__all__'
        exclude = ['case_location','note','created','modified' ]

