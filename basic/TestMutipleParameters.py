# import build_user
# from build_user import build_profile as build
from build_user import *

# def print_toppings(*toppings):
#     print(toppings)
#     pass

# print_toppings('Mushrooms', 'Hot oil', 'extra spicy')

user = build_profile('Richard', 'Huang', age=27, sex='male')

print(user)