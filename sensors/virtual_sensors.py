import random, time

# IMPORTANT: use Lists to log the values each second
def stimulate_velocity(): 
    acceleration = 9.8
    currentVelocity = 0
    velocity_log = []
    for t in range(30): # 30 seconds 
        currentVelocity = currentVelocity + acceleration
        velocity_log.append(currentVelocity)
        print(f'Time {t+1}s - Velocity: {round(currentVelocity,2)} m/s')    
        time.sleep(1)
    return velocity_log
        

def stimulate_altitude(velocity):
    currentAltitude = 0.0
    altitude_log = []
    for t in range(30):    #error in currentaltitude
        currentAltitude =  currentAltitude + velocity[t] + 1  # altitude = altitude + velocity * time_interval
        altitude_log.append(currentAltitude)
        print(f'Time {t+1}s - Altitude: {round(currentAltitude,2)} m')  
        time.sleep(1) 
    return altitude_log


def stimulate_temperature(altitude):
    # Temperature might decrease slowly as altitude goes up
    temp = 20
    temp_log = []
    for t in range(30): # 30 seconds 
        temp = temp - (altitude[t] / 10000)
        temp_log.append(temp)
        print(f'Time {t+1}s - Temperature: {round(temp,2)} °C')    
        time.sleep(1)
    return temp_log








