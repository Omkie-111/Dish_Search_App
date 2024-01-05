from django.shortcuts import render
from django.db.models import Q
from .models import Dish

def search_dish(request):
    query = request.GET.get('query')
    dishes = []

    if query:
        keywords = query.split()
        or_query = Q()
        for keyword in keywords:
            or_query |= Q(name__icontains=keyword)

        dishes = Dish.objects.filter(or_query)

    return render(request, 'search.html', {'dishes': dishes, 'query': query})
