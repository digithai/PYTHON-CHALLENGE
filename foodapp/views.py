from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils import html
from .models import Cuisine, Dish
from .forms import CuisineForm, DishForm

# Create your views here.

def cuisine(request):
    if request.method == "POST":
        form = CuisineForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/cuisine_show')
            except:
                pass
    else:
        form = CuisineForm()
    return render(request, 'index.html',{'form':form})

def dish(request,cuisine_id):
    cuisine = Cuisine.objects.get(id=cuisine_id)
    if request.method == "GET":
        form = DishForm(request.GET, request.FILES)
        return render(request, 'dish.html', {'cuisines':cuisine,'form':form})
    if request.method == "POST":
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/cuisine_show')
            except:
                pass
    else:
        form = DishForm()
    return render(request, 'dish.html',{'form':form})

def dish_insert(request):
    if request.method == "POST":
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/cuisine_show')
            except:
                pass
    else:
        form = DishForm()
    return render(request, 'dish.html',{'form':form})
# def dish_insert(request, cuisine_id):
#     cuisine = Cuisine.objects.get(id=cuisine_id)
#     if request.method == "GET":
#         return render(request, 'dish.html',{'cuisines':cuisine})
#     elif request.method == "POST":
#         form = DishForm(request.POST, request.FILES)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/cuisine_show')
#             except:
#                 pass
#         context = {'form':form}
#     else:
#         form = DishForm()
#     return render(request, 'dish.html', context)

def cuisine_show(request):
    cuisines = Cuisine.objects.all()
    return render(request,'cuisine_show.html',{'cuisines':cuisines})

def dish_show(request, cuisine_id):
    cuisine = Cuisine.objects.get(id=cuisine_id)
    return render(request,'dish_show.html', {'cuisine':cuisine})





def cuisine_edit(request, id):
    cuisines = Cuisine.objects.get(id=id)
    return render(request, 'cuisine_edit.html',{'cuisines':cuisines})

def dish_edit(request, id):
    dishes = Dish.objects.get(id=id)
    return render(request, 'dish_edit.html', {'dishes': dishes})

def cuisine_update(request, id):
    cuisines = Cuisine.objects.get(id=id)
    form = CuisineForm(request.POST, instance = cuisines)
    if form.is_valid():
        form.save()
        return redirect('/cuisine_show')
    return render(request, 'cuisine_edit.html', {'cuisines':cuisines})

def dish_update(request, id):
    dishes = Dish.objects.get(id=id)
    form = DishForm(request.POST, instance=dishes)
    if form.is_valid():
        form.save()
        return redirect("cuisine_show")

def cuisine_delete(request, id):
    cuisine = Cuisine.objects.get(id=id)
    cuisine.delete()
    return redirect('/cuisine_show')

def dish_delete(request, id):
    dish = Dish.objects.get(id=id)
    dish.delete()
    return redirect('/cuisine_show')