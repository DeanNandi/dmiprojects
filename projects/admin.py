from django.contrib import admin
from .models import Inkind, Dispensing, Brought, Cash, Purchases, Projects


@admin.register(Projects)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'email', 'date_of_creation')
    pass


@admin.register(Inkind)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'organization', 'program_name', 'quantity', 'date_supplied')
    pass


@admin.register(Dispensing)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_brand', 'organization','program_name', 'quantity', 'date_dispensed')
    pass


@admin.register(Cash)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('amount_received', 'organization', 'program_name', 'date_issued')
    pass


@admin.register(Purchases)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('item_bought', 'item_price','program_name', 'quantity', 'date_bought')
    pass


@admin.register(Brought)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('item_brought', 'item_brand', 'organization','program_name', 'quantity', 'date_brought')
    pass

