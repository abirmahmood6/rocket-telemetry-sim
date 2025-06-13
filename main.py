from sensors import virtual_sensors   

def main():
    velocity = virtual_sensors.stimulate_velocity()
    altitude = virtual_sensors.stimulate_altitude(velocity)
    temp = virtual_sensors.stimulate_temperature(altitude)

if __name__ == "__main__":
        main()


