import random


# Use random to return random virtual data for the following - 
# virtual sensors

#use random.uniform() to generate values for the virtual sensors
def get_altitude():
    return round(random.uniform(100.0,1000.0), 2)


def get_temperature():
    return round(random.uniform(-50.0,150.0), 2)


def get_velocity(): 
    return round(random.uniform(0.0,500.0), 2)


