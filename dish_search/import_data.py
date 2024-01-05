import pandas as pd
import ast
from dish_search.models import Restaurant, Dish

data = pd.read_csv('restaurants_small.csv')

for index, row in data.iterrows():
    restaurant = Restaurant.objects.create(
        name=row['name'],
        location=row['location'],
        lat_long=row['lat_long'],
        full_details=row['full_details']
    )

    items_dict = ast.literal_eval(row['items'])

    for item_name in items_dict.keys():
        Dish.objects.create(name=item_name, restaurant=restaurant)
