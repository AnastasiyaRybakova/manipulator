# Manipulator

## The package is including the official package of the Dynamixel. 

For the controlling OpenManipulator. The basic package has been modified and here the package [Dynamixel_workbench package](https://github.com/AnastasiyaRybakova/dynamixel-workbench/tree/feature/custom-position-control)  

In this package included simple code to start moving the open_manipulator arm, which made by ROBOTIS. 
Into the package included the openmanipulator package, which have been modified for prepare the manipulator for the simple motions. There is Python code for the simple move.

# Information of the manipulator

## Hardware information

To [connect](https://emanual.robotis.com/docs/en/platform/openmanipulator_x/ros_setup/#connection) the Openmanipulator, I am using the [U2D2 converter](https://emanual.robotis.com/docs/en/parts/interface/u2d2/), [power hub board](https://emanual.robotis.com/docs/en/parts/interface/u2d2_power_hub/) , and USB cable to be able to connect the robot with computer.

## How to run the code

### Testing the position control

    $ roslaunch dynamixel_workbench_controllers position_control.launch
    
There is a topic list:

    $ rostopic list
    
You will see next topics:

  - /dynamixel_state
  - /goal_dynamixel_position
  - /joint_states

      ![image](https://user-images.githubusercontent.com/37059842/113826542-40666e80-97bd-11eb-937f-a1e352cb4151.png)

And by using $rosservice list you will the list below:

  - /joint_command
  - /position_control/get_loggers
  - /position_control/set_logger_level
  
      ![image](https://user-images.githubusercontent.com/37059842/113826897-a3f09c00-97bd-11eb-8123-f78044f1f8cf.png)
      
#### How to move the arm with Python code

To move the arm with Python code we have two options:

   - We move it with a Service Client (/joint_command): We can only move one joint at a time, but it waits until movement will be finished.
   - We move it publishing in a TOpic (/goal_dynamixel_position): Moves everything at the same time, but there is no wait.

After the clonning the package of the manipulator which is includingg the Python code, we need to do some more simple steps below:

            $ cd ~/catkin_ws
            $ source devel/setup.bash
            $ rospack profile
            $ cd src/openmanipulator_move/scripts
            $ chmod +x move_openmanipulator.py
            $ cd ~/catkin_ws && catkin_make
         
#### To run the code with real robot: 

            $ roslaunch dynamixel_workbench_controllers position_control.launch
            $ rosrun openmanipulator_move move_openmanipulator.py
            





    

