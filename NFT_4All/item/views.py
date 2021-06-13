from django.shortcuts import redirect, render
from django.http import HttpResponse
from item.models import Items

def index(request):
    all_items = Items.objects.filter(bought=False)
    return render(request, 'market.html', {'all_items' : all_items})

def profile(request):
    all_items = Items.objects.filter(bought=True)
    return render(request, 'market.html', {'all_items' : all_items})

def add(request, pk):
    item = Items.objects.get(id_item=pk)
    item.bought = True
    item.save()
    return redirect('nft_profile')

def sell(request, pk):
    item = Items.objects.get(id_item=pk)
    item.bought = False
    item.save()
    return redirect('nft_list')


# Create your views here.
