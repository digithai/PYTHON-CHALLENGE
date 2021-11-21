from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils import html
from .models import Cuisine, Dish
from .forms import CuisineForm, DishForm

# Create your views here.

def cuisine_show(request):
    cuisines = Cuisine.objects.all()
    return render(request,'cuisine_show.html',{'cuisines':cuisines})

def dish_show(request, cuisine_id):
    cuisine = Cuisine.objects.get(id=cuisine_id)
    return render(request,'dish_show.html', {'cuisine':cuisine})

def cuisine(request):
    if request.method == "POST":
        form = CuisineForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = CuisineForm()
    return render(request, 'index.html',{'form':form})

def insert_dish(request, cuisine_id):
    cuisines = Cuisine.objects.get(id=cuisine_id)
    if request.method == "GET":
        # form = Dish.objects.all()
        form = DishForm(request.GET, request.FILES)
        return render(request, 'dish.html',{'cuisine':cuisines, 'form':form})
        # return render((request, 'dish.html',{'cuisine':cuisines,'form':form}))
    if request.method == "POST":
        form = DishForm(request.POST, files=request.FILES )
        
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass    
    return render(request, 'dish.html', {'cuisine':cuisines, 'form':form})

def update_cuisine(request, id):
    cuisine = Cuisine.objects.get(id=id)
    form = CuisineForm(request.POST or None, instance=cuisine)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'cuisine_update.html', {'form':form})

def update_dish(request, id):
    dish = Dish.objects.get(id=id)
    form = DishForm(request.POST or None, instance=dish)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'dish_update.html', {'form':form})

def delete_dish(request, id):
    dish = Dish.objects.get(id=id)
    if request.method == "POST":
        dish.delete()
        return redirect('/')
    return render(request, "dish_delete.html")

def delete_cuisine(request, id):
    cuisine = Cuisine.objects.get(id=id)
    if request.method == "POST":
        cuisine.delete()
        return redirect('/')
    return render(request, "cuisine_delete.html")