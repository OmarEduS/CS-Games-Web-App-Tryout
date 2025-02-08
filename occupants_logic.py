import json
from data import rooms
# Here is a method signature to get you started.

def check_occupants(room_number, date):
    # Iterating throught the rooms and the occupants to check the date and to check if the room 
    # is available
    for occupant in rooms[room_number]['occupants']:
        if occupant['check_in'] <= date <= occupant['check_in']:
            return occupant
        else:
            return []