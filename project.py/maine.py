destinations = ["Park", "Downtown", "Home", "Scenic Area"]
restaurants = ["Cheesecake Factory", "Black-Eyed Pea", "Torres", "Tacos Rapidos"]
transportations = ["Train", "Car", "Uber", "Scooter"]
entertainments = ["Arcade", "Movies", "Concert", "Sports Game"]

import random

destination = random.choice(destinations)
print(destination)
user_input = input("Sound Good? y/n: ") 


if user_input == "n":
    destination = random.choice(destinations)
    print(destination)
else:
    user_input == "y"
    print('Next!')



# restaurant = random.choice(restaurants)
# print(restaurant)


# for destination in destinations:
#     print(destinations)
