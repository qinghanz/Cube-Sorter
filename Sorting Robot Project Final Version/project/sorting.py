#!/usr/bin/env python3

"""
Sort foam cubes based on color.
"""

from utils.brick import Motor, configure_ports, EV3ColorSensor
from logic import add_color_to_queue
from time import sleep

# Parameter initialization
MAX_CUBES = 6
color_dict = {}
target_color = ""

# Hardware initialization
CHIMNEY_SENSOR = configure_ports(PORT_1=EV3ColorSensor)
CENTRAL_MOTOR, CHIMNEY_MOTOR = configure_ports(PORT_A=Motor, PORT_B=Motor)

# Initialize motors
def init_motors():
    """
    Initialize the two motors responsible for the sorting process.
    """
    try:
        CENTRAL_MOTOR.set_limits(dps=360)
        #CHIMNEY_MOTOR.set_power(20)
        CHIMNEY_MOTOR.set_limits(dps=340)
        
    except BaseException as e:
        pass


# Function to turn central motor CCW, i.e. target color location
def turn_central_motor_CCW():
    """
     Turn central motor counterclockwise. 
    """
    CENTRAL_MOTOR.set_position_relative(-90)
    CENTRAL_MOTOR.wait_is_moving()
    

# Function to turn central motor CW, i.e. undesired color location
def turn_central_motor_CW():
    """
    Turn central motor clockwise.
    """
    CENTRAL_MOTOR.set_position_relative(90)
    CENTRAL_MOTOR.wait_is_moving()
    
    
# Function to move chimney motor to push cube
def turn_chimney_motor():
    
    """
    Turns the chimney motor back and forth to push cube and reset for next sorting step.
    """
    # extend lego piece to push cube by rotating CCW
    CHIMNEY_MOTOR.set_position_relative(56)
    CHIMNEY_MOTOR.wait_is_moving()
    # sleep
    sleep(1)
    # retract lego piece by rotating CW
    CHIMNEY_MOTOR.set_position_relative(-55)
    CHIMNEY_MOTOR.wait_is_moving()
    sleep(1)
    


# Function to read colored cubes that are dropped from chimney and push them in order to sort them
def read_color_data_from_chimney():
    """
    Collect color sensor data from chimney and sort the cubes.
    """
    num_cubes = 0
    try:
        #first backwards motion of motor
        CHIMNEY_MOTOR.set_position_relative(-45)
        CHIMNEY_MOTOR.wait_is_moving()
        # sleep
        sleep(1)
        while True:
            if num_cubes == MAX_CUBES:
                CHIMNEY_MOTOR.set_position_relative(35)
                break
            color_data = CHIMNEY_SENSOR.get_color_name()  # detected color from chimney color sensor
            if color_data is not None:
                print(color_data)
                sleep(1)
                if color_data =="Red":
                    add_color_to_queue(color_dict, color_data)
                    # turn central motor to the left 
                    turn_central_motor_CW()
                    sleep(2)
                    turn_chimney_motor()
                    sleep(2)
                    # readjust to central position
                    turn_central_motor_CCW()
                    sleep(1)
                    
                elif color_data == "Green":
                    add_color_to_queue(color_dict, color_data)
                    # turn central motor to the right
                    turn_central_motor_CCW()
                    sleep(2)
                    turn_chimney_motor()
                    sleep(2)
                    # readjust to central position
                    turn_central_motor_CW()
                    sleep(1)

                elif color_data == "Blue":
                    add_color_to_queue(color_dict, color_data)
                    sleep(2)
                    turn_chimney_motor()
                   
                    sleep(1)
                else: 
                    continue
                # increment number of cubes
                num_cubes += 1
                if num_cubes == 1:
                    CHIMNEY_MOTOR.set_limits(dps=310)

    # capture all exceptions including KeyboardInterrupt (Ctrl-C)
    except BaseException as e:
        pass
    finally:
        print("Done sorting process")
        exit()
       

if __name__ == "__main__":
    # initialize motors
    init_motors()
    
    # sort cubes
    print("Starting shoe sorting system...")
    read_color_data_from_chimney()
