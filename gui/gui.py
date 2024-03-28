# PYTHON 3.9.6
import customtkinter as ctk
from helpers import *

# PROJECT DOCS
# https://docs.google.com/document/d/1nPIF0tEGJduzCj4uC4_EYdg9k11v1ASdr1NoHzhgJb8/edit

#Functions for buttons
def testFunction():
    #TODO make drone emergency land.
    print("test")

#take off function
def takeOff():
    print("Take off")

#function to land
def land():
    print("Land")

#function to increase alt/go up
def increaseAlt():
    print("Increase Alt")

#function to decrease alt/go down
def decreaseAlt():
    print("Decrease Alt")

#function to turn right
def turnRight():
    print("Turn Right")
    
#function to yaw right
def yawRight():
    print("Yaw Right")

#function to trigger movements
    
#Square Shape
def movement1():
    print("Movement 1")
    
def movement2():
    print("Movement 2")

def movement3():
    print("Movement 3")

def movement4():
    print("Movement 4")

#function to turn left
def turnLeft():
    print("Turn Left")
    
#function to yaw left
def yawLeft():
    print("Yaw Left")

#emergency button
#KILLS ALL ENGINES
def emergency():
    print("Killing all engines")




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
    
    batteryLabel = ctk.CTkLabel(innerWestFrame, text="Battery")
    batteryPercentageLabel = ctk.CTkLabel(innerWestFrame, text="p%", text_color="gray")
    
    altitudeLabel = ctk.CTkLabel(innerWestFrame, text="Altitude (cm)")
    altitudeValueLabel = ctk.CTkLabel(innerWestFrame, text="1000", text_color="gray")
    
    speedLabel = ctk.CTkLabel(innerWestFrame, text="Speed (cm/s)")
    speedValueLabel = ctk.CTkLabel(innerWestFrame, text="100", text_color="gray")
    
    emergencyButton = ctk.CTkButton(outerWestFrame, text="Emergency", width=100, height=30, command=emergency())
    
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

    turnLeftButton = ctk.CTkButton(innerLeftFrame, text="turn left", command=turnLeft())
    yawLeftButton = ctk.CTkButton(innerLeftFrame, text="yaw left", command=yawLeft())

    turnLeftButton.pack(ipadx=25, ipady=10, pady=7)
    yawLeftButton.pack(ipadx=25, ipady=10, pady=7)

#######################################################################################################
    # Create the turn right frame
    innerRightFrame, outerRightFrame = createNiceFrame(win, x=200, y=200)

    turnRightButton = ctk.CTkButton(innerRightFrame, text="turn right", command=turnRight())
    yawRightButton = ctk.CTkButton(innerRightFrame, text="yaw right", command=yawRight())

    turnRightButton.pack(ipadx=25, ipady=10, pady=7)
    yawRightButton.pack(ipadx=25, ipady=10, pady=7)

#######################################################################################################
    # Create the preprogrammed buttons frame (MOVEMENTS FRAME)
    #TODO
    innerSouthFrame, outerSouthFrame = createNiceFrame(win, x=500, y=200)
    preprogrammedButtons = []
    for i in range(4):
        preprogrammedButtons.append(ctk.CTkButton(innerSouthFrame, width=200, height=40, text="Movement " + str(i + 1), command=movement1))
        # WHEN THE FUNCTION OF THIS BUTTON IS ASSIGNED, BE SURE TO ASSIGN CORRECT COMMANDS AS WELL
    
    preprogrammedButtons[0].grid(row=0, column=0, padx=10, pady=10)
    preprogrammedButtons[1].grid(row=0, column=1, padx=10, pady=10)
    preprogrammedButtons[2].grid(row=1, column=0, padx=10, pady=0)
    preprogrammedButtons[3].grid(row=1, column=1, padx=10, pady=0)
    

#######################################################################################################
    # Create the controls frame on the east
    innerEastFrame, outerEastFrame = createNiceFrame(win, x=200, y=400)

    takeOffButton = ctk.CTkButton(innerEastFrame, text="take off", command=takeOff)
    landButton = ctk.CTkButton(innerEastFrame, text="land", command=testFunction)
    increaseAltitudeButton = ctk.CTkButton(innerEastFrame, text="+ Altitude", command=increaseAlt())
    decreaseAltitudeButton = ctk.CTkButton(innerEastFrame, text="- Altitude", command=decreaseAlt())

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