# import_data.py

import csv
from dish_search.models import Dish

with open('restaurants_small.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Dish.objects.create(
            name=row['name'],
            location=row['location'],
            items=row['items'],
            lat_long=row['lat_long'],
            full_details=row['full_details']
        )
