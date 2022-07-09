# ECSE211 Project: Team 11 - EV<sup>3</sup> Sorter


## Project Software Overview

Two BrickPi's are used in our implementation, each running a different script. The sorting process happens on the first BrickPi, where the **`sorting.py`** script is executed. A color sensor detects a color and triggers a motor which pushes it to a surface. Depending on the color that is read from the sensor, this surface will rotate in a specific direction, where the cube can fall onto a unique slope. Consequently, three different colored cubes will fall onto three different slopes. When the script terminates, the colors will be sorted within these slopes.

The second BrickPi will be responsible for the retrieval process, which is triggered by executing the **`retriever.py`** script. A request occurs when placing a cube in front of a color sensor and pressing the button on the touch sensor. Depending on the color that is detected by the color sensor, a single cube will be pushed from one of the three slopes mentioned above into the delivery area.
___

## Project Organization

In this section, we go over the files and folders included in this project,
listed in alphabetical order.
The files we modified are shown in **bold**.

- `lib`: contains libraries used by the robot such as
  the simpleaudio sound library.
- `project`: all Python files in this folder run on the robot.
  - [`doc`](project/doc): documentation for the brick API
  (Application Programming Interface), ie, the classes and functions
  you can use to work with the robot.
  - [`utils`](project/utils): brick-related utilities for this project.
  See the other project files to see examples of how to use these modules.
    - `brick.py`: the main module for interacting with the brick hardware.
    - `sound.py`: module that allows you to play sounds.
    It depends on the simpleaudio library.
  - [**`logic.py`**](project/logic.py): computations that can run on both
  the brick and the computer. Placing these in a separate file allows
  for testing on a computer, which can be faster than running on the brick.
   - [**`sorting.py`**](project/sorting.py): Handles the sorting process of the cubes before the initial request.
  The colors involved are Red, Blue, and Green, and each color will be sorted into a unique area. 
  - [**`retriever.py`**](project/retriever.py):
  _ Handles retrieving a single cube that is requested from the request area. Depending on the requested color, 
 the appropriate motor will be triggered and push a cube of that color to the delivery area.
  - [**`test_logic.py`**](project/test_logic.py): a script to test the correctness of controller logic.
  It is meant to be run from a computer using the `pytest` command.
- `scripts`:
  - `reset_brick.py`: If the program does not exit correctly, eg,
  if it is stuck in an infinite loop, this script can be run on the brick to reset it.
- `deploy_to_robot.py`: a script to deploy the code to the robot from a computer.
  It offers the following options:
  - Deploy DPM Project on Robot without running:
  copy the `project` folder to the robot.
  - Deploy and run DPM Project on Robot:
  copy the `project` folder to the robot and run the file specified
  in `project_info.json`.
  - Reset Robot: reset the robot.
- **`project_info.json`**: a file containing information about the project.
- `robot_setup.sh`: a script to install the required libraries on
the brick as described in the project instructions.
