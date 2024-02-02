# car_rental/views.py
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CarForm, SignUpForm
from .models import Car
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Car
from .forms import CarBrandFilterForm

def car_list(request):
    # Get all cars initially
    cars = Car.objects.all()

    # Handle brand filter if provided in the request
    brand_filter = request.GET.get('brand', '')
    if brand_filter:
        cars = cars.filter(brand=brand_filter)

    # Retrieve unique brand values for the filter dropdown
    brands = Car.objects.values_list('brand', flat=True).distinct()

    # Context data to pass to the template
    context = {
        'cars': cars,
        'brands': brands,
        'brand_filter': brand_filter,
    }

    return render(request, 'car_rental/car_list.html', context)

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'car_rental/car_detail.html', {'car': car})

@login_required
def car_new(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm()
    return render(request, 'car_rental/car_edit.html', {'form': form})

def success(request):
    return HttpResponse('successfully uploaded')


""" @login_required
def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            messages.success(request, 'Car updated successfully!')
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm(instance=car)
    return render(request, 'car_rental/car_edit.html', {'form': form})
 """
 
@login_required
def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            messages.success(request, 'Car updated successfully!')
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm(instance=car)

    return render(request, 'car_rental/car_edit.html', {'form': form})


@login_required
def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()
    messages.success(request, 'Car deleted successfully!')
    return redirect('car_list')

def home(request):
    return render(request, 'car_rental/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('car_list')
    else:
        form = AuthenticationForm()
    return render(request, 'car_rental/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'car_rental/signup.html', {'form': form})

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy('home'))