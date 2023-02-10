import random

destinations = ["Park", "Downtown", "Home", "Scenic Area"]
restaurants = ["Cheesecake Factory", "Black-Eyed Pea", "Torres", "Tacos Rapidos"]
transportations = ["Train", "Car", "Uber", "Scooter"]
entertainments = ["Arcade", "Movies", "Concert", "Sports Game"]


def day_trip(list):
    user_input = ""
    while user_input != "y":
        random_selection = random.choice(list)
        print(random_selection)
        user_input = input("Sound Good? type y/n: ")
    return random_selection


destination = day_trip(destinations)
restaurant = day_trip(restaurants)
transportation = day_trip(transportations)
entertainment = day_trip(entertainments)

# date_night = (destinations), (restaurants), (transportations), (entertainments)

def confirm_trip():
    print()
    confirmation_list = print(f"Your destination is {destination}, \nYour restaurant is {restaurant}, \nYour mode of transportation is {transportation}, \nYour form of entertainment is {entertainment}")
    print()
    user_input = input("This is your complete trip. Are you happy with the selection? type y/n: ")
    while user_input != 'y':
            newdest = day_trip(destinations)
            newrest = day_trip(restaurants)
            newtransport = day_trip(transportations)
            newtainment = day_trip(entertainments)
            print()
            print(f"Here is your list, have a good one! \n Destination: {newdest} \n Restaurant: {newrest} \n Transportation: {newtransport} \n Entertainment: {newtainment}")
            print()
            
          
            
    if user_input == "y":
        print(f"Here is your list, have a good one! \n Destination: {destination} \n Restaurant: {restaurant} \n Transportation: {transportation} \n Entertainment: {entertainment}")

    
        


        return confirmation_list

    


confirm_trip()
