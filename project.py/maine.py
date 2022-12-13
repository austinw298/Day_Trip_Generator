destinations = ["Park", "Downtown", "Home", "Scenic Area"]
restaurants = ["Cheesecake Factory", "Black-Eyed Pea", "Torres", "Tacos Rapidos"]
transportations = ["Train", "Car", "Uber", "Scooter"]
entertainments = ["Arcade", "Movies", "Concert", "Sports Game"]

import random


# while user_input == 'n':
#     destination = random.choice(destinations)
#     print(destination)
#     user_input = input("Sound Good? y/n: ") 

def day_trip(step):
    user_input = random.choice(step)
    while user_input == input("n"):
        part = random.choice(step)
        print(part)
        user_input = input("Sound good? y/n ")
    return


# def trip_day(step):
#     user_input = input("start")
#     if user_input == 'n':
#         destination = random.choice(step)
#         print(destination)
#         user_input = input(f"Does {step} work? ")
#     elif user_input == 'y':
#         print('next')
#         return
    

# trip_day(destinations)

day_trip(destinations)
# day_trip(restaurants)
# day_trip(transportations)
# day_trip(entertainments)

# if user_input == "n":
#     destination = random.choice(destinations)
#     print(destination)
# else:
#     user_input == "y"
#     print('Next!')



# restaurant = random.choice(restaurants)
# print(restaurant)
