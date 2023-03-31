from django.shortcuts import render, redirect
from .models import Projects, Cash, Purchases, Inkind, Dispensing, Brought
from .forms import MyForm, Inkind_form, cash_form, purchases_form, Brought_form, Dispensing_form
from .filters import OrderFilter, OrderFilter2, OrderFilter3, OrderFilter4, OrderFilter5
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('/')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def new_projects(request):
    return render(request, 'new-projects.html', {})


def inkind(request):
    inkind = Inkind.objects.all()

    myFilter = OrderFilter(request.GET, queryset=inkind)
    inkind = myFilter.qs

    context = {'inkind': inkind,'myFilter': myFilter,}
    return render(request, 'inkind.html', context)

def dispenses_report(request):
    dispensing = Dispensing.objects.all()

    myFilter = OrderFilter2(request.GET, queryset=dispensing)
    dispensing = myFilter.qs

    context = {'dispensing': dispensing,'myFilter': myFilter,}
    return render(request, 'dispensing.html', context)

def purchases_report(request):
    purchases = Purchases.objects.all()

    myFilter = OrderFilter3(request.GET, queryset=purchases)
    purchases = myFilter.qs

    context = {'purchases': purchases,'myFilter': myFilter,}
    return render(request, 'purchases.html', context)


def cash_report(request):
    cash = Cash.objects.all()

    myFilter = OrderFilter4(request.GET, queryset=cash)
    cash = myFilter.qs

    context = {'cash': cash,'myFilter': myFilter,}
    return render(request, 'cash.html', context)

def broughts_report(request):
    brought = Brought.objects.all()

    myFilter = OrderFilter5(request.GET, queryset=brought)
    brought = myFilter.qs

    context = {'brought': brought,'myFilter': myFilter,}
    return render(request, 'brought.html', context)


def index(request):
    projects = Projects.objects.all()

    myFilter = OrderFilter(request.GET, queryset=projects)
    projects = myFilter.qs

    total_projects = projects.count()

    context = {'projects': projects, 'myFilter': myFilter, 'total_projects': total_projects}

    return render(request, 'index.html', context)

def delete_project(request, pk):

    template = 'index.html'
    Projects.objects.filter(id=pk).delete()

    projects = Projects.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, template, context)


def delete_inkind(request, pk):

    template = 'inkind.html'
    Inkind.objects.filter(id=pk).delete()

    inkind = Inkind.objects.all()

    context = {
        'inkind': inkind,
    }

    return render(request, template, context)

def delete_dispensing(request, pk):

    template = 'dispensing.html'
    Dispensing.objects.filter(id=pk).delete()

    dispensing = Dispensing.objects.all()

    context = {
        'dispensing': dispensing,
    }

    return render(request, template, context)

def delete_purchases(request, pk):

    template = 'purchases.html'
    Purchases.objects.filter(id=pk).delete()

    purchases = Purchases.objects.all()

    context = {
        'purchases': purchases,
    }

    return render(request, template, context)

def delete_cash(request, pk):

    template = 'cash.html'
    Cash.objects.filter(id=pk).delete()

    cash = Cash.objects.all()

    context = {
        'cash': cash,
    }

    return render(request, template, context)

def delete_brought(request, pk):

    template = 'brought.html'
    Brought.objects.filter(id=pk).delete()

    brought = Brought.objects.all()

    context = {
        'brought': brought,
    }

    return render(request, template, context)

def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
  else:
      form = MyForm()
  return render(request, 'cv-form.html', {'form': form})


def giving_form(request):
  if request.method == "POST":
    form = Inkind_form(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
  else:
      form = Inkind_form()
  return render(request, 'cv-form.html', {'form': form})


def form_cash(request):
  if request.method == "POST":
    form = cash_form(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
  else:
      form = cash_form()
  return render(request, 'cv-form.html', {'form': form})


def form_purchase(request):
  if request.method == "POST":
    form = purchases_form(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
  else:
      form = purchases_form()
  return render(request, 'cv-form.html', {'form': form})

def brought_form(request):
  if request.method == "POST":
    form = Brought_form(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
  else:
      form = Brought_form()
  return render(request, 'cv-form.html', {'form': form})


def form_dispense(request):
  if request.method == "POST":
    form = Dispensing_form(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
  else:
      form = Dispensing_form()
  return render(request, 'cv-form.html', {'form': form})