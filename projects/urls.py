from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('projects-form', views.my_form, name='projects-form'),
    path('inkind-form', views.giving_form, name='inkind-form'),
    path('cash-form', views.form_cash, name='cash-form'),
    path('purchases-form', views.form_purchase, name='purchases-form'),
    path('brought-form', views.brought_form, name='brought-form'),
    path('dispensing-form', views.form_dispense, name='dispensing-form'),
    path('new-projects', views.new_projects, name="new-projects"),
    path('inkind-report', views.inkind, name="inkind-report"),
    path('dispensing-report', views.dispenses_report, name="dispensing-report"),
    path('purchases-report', views.purchases_report, name="purchases-report"),
    path('cash-report', views.cash_report, name="cash-report"),
    path('brought-report', views.broughts_report, name="brought-report"),
    path('login', views.loginPage, name="login"),
    path('register', views.registerPage, name="register"),
    path('logout', views.logoutUser, name="logout"),
    path('delete-projects/(?P<pk>\d+)', views.delete_project, name='delete-projects/(?P<pk>\d+)'),
    path('delete-inkind/(?P<pk>\d+)', views.delete_inkind, name='delete-inkind/(?P<pk>\d+)'),
    path('delete-dispensing/(?P<pk>\d+)', views.delete_dispensing, name='delete-dispensing/(?P<pk>\d+)'),
    path('delete-purchases/(?P<pk>\d+)', views.delete_purchases, name='delete-purchases/(?P<pk>\d+)'),
    path('delete-cash/(?P<pk>\d+)', views.delete_cash, name='delete-cash/(?P<pk>\d+)'),
    path('delete-brought/(?P<pk>\d+)', views.delete_brought, name='delete-brought/(?P<pk>\d+)')

]
