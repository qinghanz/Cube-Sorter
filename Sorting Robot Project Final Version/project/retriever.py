#!/usr/bin/env python3

"""
Retrieve foam cubes given a certain color.
"""


from utils.brick import Motor, configure_ports, EV3ColorSensor, TouchSensor
from time import sleep
from utils.sound import Sound

# Parameter initialization
target_color = ""


# Hardware initialization
REQ_COLOR_SENSOR, TOUCH_SENSOR = configure_ports(PORT_1=EV3ColorSensor, PORT_2=TouchSensor)
PUSH_MOTOR_LEFT, PUSH_MOTOR_CENTER, PUSH_MOTOR_RIGHT = configure_ports( PORT_A=Motor, PORT_B=Motor, PORT_C=Motor)

fail_sound = Sound(duration=0.5, volume=80, pitch="C5")


def init_motors():  # Initialize motors
    """
    Initializes the three motors responsible for the retrieval process of
    the three cubes. 
    """
    try:
        PUSH_MOTOR_LEFT.set_limits(dps=580)
        PUSH_MOTOR_CENTER.set_limits(dps=360)
        PUSH_MOTOR_RIGHT.set_limits(dps=580)

    except BaseException as e:
        pass


def turn_left_motor_CCW():  # function to turn left motor counter clockwise
    """
    Turns the left motor counterclockwise.
    """
    PUSH_MOTOR_LEFT.set_position_relative(-83)
    PUSH_MOTOR_LEFT.wait_is_moving()
    sleep(1)


def turn_left_motor_CW():  # function to turn left motor clockwise
    """
    Turns the left motor clockwise.
    """
    PUSH_MOTOR_LEFT.set_position_relative(80)
    PUSH_MOTOR_LEFT.wait_is_moving()
    sleep(1)


def turn_center_motor_CCW():  # function to turn middle motor counter clockwise
    """
    Turns the center motor counterclockwise.
    """
    PUSH_MOTOR_CENTER.set_position_relative(-48)
    PUSH_MOTOR_CENTER.wait_is_moving()
    sleep(1)


def turn_center_motor_CW():  # function to turn middle motor clockwise
    """
    Turns the center motor clockwise.
    """
    PUSH_MOTOR_CENTER.set_position_relative(45)
    PUSH_MOTOR_CENTER.wait_is_moving()
    sleep(1)


def turn_right_motor_CCW():  # function to turn right motor counter clockwise
    """
    Turns the right motor counterclockwise.
    """
    PUSH_MOTOR_RIGHT.set_position_relative(-73)
    PUSH_MOTOR_RIGHT.wait_is_moving()
    sleep(1)


def turn_right_motor_CW():  # function to turn right motor clockwise
    """
    Turns the right motor clockwise.
    """
    PUSH_MOTOR_RIGHT.set_position_relative(70)
    PUSH_MOTOR_RIGHT.wait_is_moving()
    sleep(1)


# Function to read colored cubes in request area


def read_color_data_from_req():
    """
    Reads color from request area. If color is either Red, Blue, or Green, a cube is delivered.
    Otherwise, a sound is played. 
    """
    try:
        color_count = 0
        while True:
            if color_count == 6:
                break
            if TOUCH_SENSOR.is_pressed():
                # detected color from req area color sensor
                color_data = REQ_COLOR_SENSOR.get_color_name()
                rgb = REQ_COLOR_SENSOR.get_rgb()
                g_value = rgb[1]
                print(rgb)
                print(color_data)
                if color_data is not None:
                    sleep(1)  # sleep after reading a non null color
                    target_color = color_data  # set target color to detected color
                    if target_color == "Green":
                        turn_left_motor_CW()
                        turn_left_motor_CCW()
                        color_count += 1
                    elif target_color == "Blue":
                        turn_center_motor_CW()
                        turn_center_motor_CCW()
                        color_count +=1
                    elif target_color == "Red":
                        if g_value > 60:
                            fail_sound.play().wait_done()
                            continue
                        turn_right_motor_CW()
                        turn_right_motor_CCW()
                        color_count +=1
                    else:
                        fail_sound.play().wait_done()  
                        continue
                  
                    print("target cube delivered")
                    
                    
    # capture all exceptions including KeyboardInterrupt (Ctrl-C)
    except BaseException as e:
        pass
    finally:
        print("Done delivery process")
        exit()


if __name__ == "__main__":

    init_motors()

    print("Start requesting shoes...")

    # read color of cube in requested area
    read_color_data_from_req()

    # ADD REST OF METHODS HERE....
    # ...
