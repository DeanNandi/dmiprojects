import django_filters
from .models import Inkind, Dispensing, Purchases, Cash, Brought


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Inkind
        fields = '__all__'
        exclude = ['organization','quantity','date_supplied']


class OrderFilter2(django_filters.FilterSet):
    class Meta:
        model = Dispensing
        fields = '__all__'
        exclude = ['item_name','organization','quantity', 'date_dispensed']


class OrderFilter3(django_filters.FilterSet):
    class Meta:
        model = Purchases
        fields = '__all__'
        exclude = ['item_price','date_bought', 'quantity']


class OrderFilter4(django_filters.FilterSet):
    class Meta:
        model = Cash
        fields = '__all__'
        exclude = ['organization', 'date_issued']


class OrderFilter5(django_filters.FilterSet):
    class Meta:
        model = Brought
        fields = '__all__'
        exclude = ['item_brought', 'program_name', 'quantity', 'date_brought']

