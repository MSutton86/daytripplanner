import random

destinations = ['San Francisco', 'New York', 'Chicago']
restaurants = ['Pizza', 'Sushi', 'Burgers']
transportations = ['Uber', 'Subway', 'Lamborfitis']
entertainments = ['Live MUsic', 'Historic Theatre', 'Shopping']

entertainment = random.choice(entertainments)
transportation = random.choice(transportations)
restaurant = random.choice(restaurants)
destination = random.choice(destinations)

your_trip = (destination, restaurant, transportation, entertainment)
print(your_trip)

is_it = False

is_it = input("Is this your trip? y/n ")

while is_it != 'y':
    print(your_trip)
    is_it = input("is this your trip? y/n ")
    

print("Have fun! Safe travels!")