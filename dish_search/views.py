from django.shortcuts import render
from .models import Dish

def search_dish(request):
    query = request.GET.get('query')
    if query:
        dishes = Dish.objects.filter(name__icontains=query)
    else:
        dishes = []

    context = {
        'query': query,
        'dishes': dishes
    }
    return render(request, 'search.html', context)
