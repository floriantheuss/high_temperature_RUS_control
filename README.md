# high_temperature_RUS_control
control of the high temperature resonant ultrasound spectroscopy setup;
i.e. connection to a Raspberry Pie to perform the following tasks:
  - control of the hot plate (to change the temperature)
  - control of the power relay (as a remote on/off switch)
  - control of Raspberry Pi camera module for surveillance


## General Remarks

General access:
  - from your terminal, you can access the Pi's terminal by typing: ssh pi@10.84.241.104 (ssh pi@raspberrypi.lassp.cornell.edu is also ok) - the password is: chill
  - the relevant python code is stored in "Documents/high_T_RUS". You can access this folder by typing "cd Documents/high_T_RUS" in the Raspberry Pi terminal

some useful keywords to navigate the Linux terminal:
  - cd <directory>: change directory to given directory (if no directory is given, you are going back to the highest level)
  - dir: show all files in the current directory
  - mv <direcotry 1> <direcotry 2>: rename directory 1 to directory 2
  - rm <filename>: delete a file
  - cp <filename 1> <filename 2>: copy file 1 and rename it file 2
  - touch <filename>: creates a file in the current directory
  - nano <filename>: opens a file in the text editor nano
 

## How to run code

to control any of these instruments open python3 in the directory and type:
  - from high_T_RUS import StepperMotor, PowerRelay, CameraModule

detailed information about the kinds of classes and functions defined for them can be found below

### about the camera module:
  - camera = CameraModule()
  - camera.show(seconds=5) #shows a live video captured by the camera; 
                         # by default, the video is show
  - the Raspberry Pi's livestream can be accessed by typing "http://10.84.241.104:8081" into a web browser


### about the stepper motor:
  - sm = StepperMotor(position=0) #initializes the stepper motor; it's initial position 
  is set to 0, but can be adjusted and given a specific angle
  - sm.get_angle() #gives the current angle of the stepper motor
  - sm.set_new_zero() #labels the current position of the stepper motor as "zero"
  - sm.turn(angle, direction) turn the stepper motor by an "angle" in a certain "direction"  -- options are 'cw'/'ccw' for clockwise/counterclockwise
  - sm.set_angle(angle) #set the angle of the stepper motor to a specific "angle";
  angles are counted clockwise starting from the "zero" position of the stepper motor
  - sm.set_dial(number) #set the stepper motor to a certain angle, such that the dial of the hot plate is at "number"
  - sm.end() #turn stepper motor to its "zero" position; NOTE THAT IT ALSO TURNS OFF THE CONTROL OF THE POWER RELAY
  #### there is some slack between the stepper motor and the actualy hot plate dial, which makes the set_angle/set_number functions inaccurate; I would only use .turn and monitor what happens with the webcam
  
### about the power relay:
  - pr = PowerRelay() #initializes an instance of power relay
  - pr.mode(mode) #you can turn the power relay "on" or "off" - 'on' turns the 'normally off' outlets on ('off' turns/leaves them off)
  

