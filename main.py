from sensors import virtual_sensors    #import virtual sensors from sensors file

def main():
    altitude = virtual_sensors.get_altitude()
    temp = virtual_sensors.get_temperature()
    velocity = virtual_sensors.get_velocity()


    print('🚀 Rocket Telemetry Data: \n' )
    print(f'Rocket Altitude: {altitude} m \n' )
    print(f'Rocket Temperature: {temp} C\n' )
    print(f'Rocket Velocity: {velocity} m/s\n' )


if __name__ == "__main__":
        main()

