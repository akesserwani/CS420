# PYTHON 3.9.6
import customtkinter as ctk
from helpers import *
from djitellopy import Tello
import cv2


# PROJECT DOCS
# https://docs.google.com/document/d/1nPIF0tEGJduzCj4uC4_EYdg9k11v1ASdr1NoHzhgJb8/edit

#Initialize drone 
tello = Tello()

tello.connect()



#Functions for buttons

#take off function
def takeOff():
    print("Take off")

    tello.takeoff()


#function to land
def land():
    print("Land")

    tello.land()


#function to increase alt/go up
def increaseAlt():
    print("Increase Alt")

    tello.move_up(50)

#function to decrease alt/go down
def decreaseAlt():
    print("Decrease Alt")

    tello.move_down(50)

#function to turn right
def turnRight():
    print("Turn Right")

    tello.move_right(50)
    
#function to yaw right
def yawRight():
    print("Yaw Right")

    tello.rotate_clockwise(50)

#function to turn left
def turnLeft():
    print("Turn Left")

    tello.move_left(50)
    
#function to yaw left
def yawLeft():
    print("Yaw Left")
    
    tello.rotate_counter_clockwise(50)

#function to trigger movements
    
#Front Flip
def movement1():
    tello.flip_forward()

#Back Flip
def movement2():
    tello.flip_back()

#Square
def movement3():
    tello.move_up(100)
    tello.move_right(100)
    tello.move_down(100)
    tello.move_left(100)

#Rectangle
def movement4():
    tello.move_up(100)
    tello.move_right(150)
    tello.move_down(100)
    tello.move_left(150)
    

#emergency button
#KILLS ALL ENGINES
def emergency():
    print("Killing all engines")

    tello.emergency()



#functions for active text
#text will update every 5 seconds
#get_battery()
def updateBattery(batteryLabel):
    #get battery level 
    battery_level = tello.get_battery()  
    #configure the batteryLabel which is the parameter passed 
    batteryLabel.configure(text=f"{battery_level}%", text_color="gray")  
    #batter label updates every 1000 miliseconds -> 1 second
    #call recursively to update

    batteryLabel.after(1000, lambda: updateBattery(batteryLabel))  
    
#get_barometer() -> displays in cm
def updateAlt(altLabel):
    #get barometer level
    current_alt = tello.get_barometer()
    #subtract locationAlt from current alt to get absolute altitude relative to level
    # current_alt -= locationAlt

    #convert to feet
    #1 foot = 30.48 cm
    # current_alt = current_alt / 30.48
    #configure the altLabel which is the parameter passed
    altLabel.configure(text=f"{round(current_alt)}", text_color="gray")  
    #alt label updates every 100 miliseconds -> 0.1 second
    #call recursively to update

    altLabel.after(1000, lambda: updateAlt(altLabel))  

#get_speed_x() => cm/s
def updateSpeed(speedLabel):
    #get speed
    current_speed = tello.get_speed_y()
    #configure speed label
    speedLabel.configure(text=f"{current_speed}", text_color="gray")  
    #alt label updates every 100 miliseconds -> 0.1 second
    #call recursively to update
    speedLabel.after(1000, lambda: updateSpeed(speedLabel))  





#main function for the UI
def main():
    # set theme to our custom theme
    # see this for more information:    https://customtkinter.tomschimansky.com/documentation/color

    pathToTheme = "gui/customtheme.json"
    ctk.set_default_color_theme(pathToTheme)

    # create main window
    win = ctk.CTk()
    win.resizable(False, False)     # main window cannot be resized
    win.title("Aerial Ace")         # sets the title fo the window to "Aerial Ace"
    win.geometry("1010x510")        # sets default dimensions of the main window
    win.iconbitmap(None)            # set tkinter icon (can change later TODO)

####################################################################################################
    # Create the active data frame to put on the west side of the main window
    innerWestFrame, outerWestFrame  = createNiceFrame(win, x=800, y=400)
    
    #text for battery label
    #define global variable to be accessed outside main in updateBattery()
    global batteryPercentageLabel
    #label for "Battery" text
    batteryLabel = ctk.CTkLabel(innerWestFrame, text="Battery")
    #main label for the changing percentage value
    batteryPercentageLabel = ctk.CTkLabel(innerWestFrame, text="p", text_color="gray")
    #batteryPercentageLabel is passed as a parameter to be changed every 1 second
    updateBattery(batteryPercentageLabel)

    #text for altitude label
    #define global variable
    global altitudeValueLabel
    #label for altitude text
    altitudeLabel = ctk.CTkLabel(innerWestFrame, text="Altitude (ft)")
    #main label displaying changing altitude value
    altitudeValueLabel = ctk.CTkLabel(innerWestFrame, text="1000", text_color="gray")
    #altitudeValueLabel is passed as parameter to be changed every 100 milisecond, 0.1 seconds
    #pass a second variable as the starting altitude, this will be subtracted to find the absolute altitude, not sea level 
    #locationAlt = tello.get_barometer()
    updateAlt(altitudeValueLabel)
    
    #text for speed label
    #define global variable
    global speedValueLabel
    #label for speed text
    speedLabel = ctk.CTkLabel(innerWestFrame, text="Speed (cm/s)")
    #main label displaying changing speed value
    speedValueLabel = ctk.CTkLabel(innerWestFrame, text="100", text_color="gray")
    #speedValueLabel passed as parameter to be changed every 100 milisecond, 0.1 seconds
    updateSpeed(speedValueLabel)

    #emergency button
    emergencyButton = ctk.CTkButton(outerWestFrame, text="Emergency", width=100, height=30, command=emergency)
    
    leftColPaddingX = 25
    PaddingY = 20
    rightColPaddingX = 10
    
    batteryLabel.grid(row=0, column=0, ipadx=leftColPaddingX, ipady=PaddingY, sticky="w")
    batteryPercentageLabel.grid(row=0, column=1, ipadx=rightColPaddingX, ipady=PaddingY)
    
    altitudeLabel.grid(row=1, column=0, ipadx=leftColPaddingX, ipady=PaddingY, sticky="w")
    altitudeValueLabel.grid(row=1, column=1, ipadx=rightColPaddingX, ipady=PaddingY)
    
    speedLabel.grid(row=2, column=0, ipadx=leftColPaddingX, ipady=PaddingY, sticky="w")
    speedValueLabel.grid(row=2, column=1, ipadx=rightColPaddingX, ipady=PaddingY)
    
    emergencyButton.pack(ipadx=leftColPaddingX, ipady=10)

#######################################################################################################
    # Create the turn left frame
    innerLeftFrame, outerLeftFrame = createNiceFrame(win, x=200, y=200)

    turnLeftButton = ctk.CTkButton(innerLeftFrame, text="turn left", command=turnLeft)
    yawLeftButton = ctk.CTkButton(innerLeftFrame, text="yaw left", command=yawLeft)

    turnLeftButton.pack(ipadx=25, ipady=10, pady=7)
    yawLeftButton.pack(ipadx=25, ipady=10, pady=7)

#######################################################################################################
    # Create the turn right frame
    innerRightFrame, outerRightFrame = createNiceFrame(win, x=200, y=200)

    turnRightButton = ctk.CTkButton(innerRightFrame, text="turn right", command=turnRight)
    yawRightButton = ctk.CTkButton(innerRightFrame, text="yaw right", command=yawRight)

    turnRightButton.pack(ipadx=25, ipady=10, pady=7)
    yawRightButton.pack(ipadx=25, ipady=10, pady=7)

#######################################################################################################
    # Create the preprogrammed buttons frame (MOVEMENTS FRAME)
    innerSouthFrame, outerSouthFrame = createNiceFrame(win, x=500, y=200)
    preprogrammedButtons = []
    programmedButtonFunctions = [movement1, movement2, movement3, movement4]
    buttonNames = ["Front Flip", "Back Flip", "Square", "Rectangle"]

    for i in range(4):
        preprogrammedButtons.append(ctk.CTkButton(innerSouthFrame, width=200, height=40, text=buttonNames[i], command=programmedButtonFunctions[i]))
        # WHEN THE FUNCTION OF THIS BUTTON IS ASSIGNED, BE SURE TO ASSIGN CORRECT COMMANDS AS WELL
    
    preprogrammedButtons[0].grid(row=0, column=0, padx=10, pady=10)
    preprogrammedButtons[1].grid(row=0, column=1, padx=10, pady=10)
    preprogrammedButtons[2].grid(row=1, column=0, padx=10, pady=0)
    preprogrammedButtons[3].grid(row=1, column=1, padx=10, pady=0)
    

#######################################################################################################
    # Create the controls frame on the east
    innerEastFrame, outerEastFrame = createNiceFrame(win, x=200, y=400)

    takeOffButton = ctk.CTkButton(innerEastFrame, text="take off", command=takeOff)
    landButton = ctk.CTkButton(innerEastFrame, text="land", command=land)
    increaseAltitudeButton = ctk.CTkButton(innerEastFrame, text="+ Altitude", command=increaseAlt)
    decreaseAltitudeButton = ctk.CTkButton(innerEastFrame, text="- Altitude", command=decreaseAlt)

    takeOffButton.pack(ipadx=25, ipady=10, pady=7)
    landButton.pack(ipadx=25, ipady=10, pady=7)
    increaseAltitudeButton.pack(ipadx=25, ipady=10, pady=7)
    decreaseAltitudeButton.pack(ipadx=25, ipady=10, pady=7)

#######################################################################################################
    # Create active camera feed frame in the center
    centerFrame = ctk.CTkFrame(win, width=500, height=300, fg_color="black", border_color="white")

    


#######################################################################################################
    # widget placements using layout manager (Grid is most likely candidate since our window isn't resizeable anyways)
    outerWestFrame.grid(row=0, column=0, ipady=10, ipadx=10, padx=10, pady=20, sticky="n")
    centerFrame.grid(row=0, column=1, padx=10, pady=20, sticky="s")
    outerEastFrame.grid(row=0, column=2, ipady=10, ipadx=10, padx=10, pady=20, sticky="n")

    outerLeftFrame.grid(row=1, column=0, ipady=10, ipadx=10, padx=10)
    outerSouthFrame.grid(row=1, column=1, ipady=10, ipadx=10, padx=10, sticky="s")
    outerRightFrame.grid(row=1, column=2, ipady=10, ipadx=10, padx=10)
    #######################################################################################################
    
    win.mainloop()                  # keeps the window looping

main()