# PYTHON 3.9.6
import customtkinter as ctk

def testFunction():
    print("test")

def main():
    # set theme to our custom theme
    # see this for more information:    https://customtkinter.tomschimansky.com/documentation/color

    pathToTheme = "gui/customtheme.json"
    ctk.set_default_color_theme(pathToTheme)

    # create main window
    win = ctk.CTk()
    win.resizable(False, False)     # main window cannot be resized
    win.title("Aerial Ace")         # sets the title fo the window to "Aerial Ace"
    win.geometry("1000x500")        # sets default dimensions of the main window
    win.iconbitmap(None)            # set tkinter icon (can change later TODO)

    # Create the active data frame to put on the west side of the main window
    outerDataFrame = ctk.CTkFrame(win,
                             width=600,
                             height=400)
    innerDataFrame = ctk.CTkFrame(outerDataFrame,
                             width=800,
                             height=400,
                             border_width=0)
    
    
    batteryLabel = ctk.CTkLabel(innerDataFrame, text="Battery")
    batteryPercentageLabel = ctk.CTkLabel(innerDataFrame, text="p%", text_color="gray")
    
    altitudeLabel = ctk.CTkLabel(innerDataFrame, text="Altitude (cm)")
    altitudeValueLabel = ctk.CTkLabel(innerDataFrame, text="1000", text_color="gray")
    
    speedLabel = ctk.CTkLabel(innerDataFrame, text="Speed (cm/s)")
    speedValueLabel = ctk.CTkLabel(innerDataFrame, text="100", text_color="gray")
    
    emergencyButton = ctk.CTkButton(outerDataFrame, text="Emergency", width=100, height=30, command=testFunction)

    # Create the LED frame
    #TODO

    # Create the preprogrammed buttons frame
    #TODO

    # Create the controls frame on the east
    #TODO

    # Create active camera feed frame in the center
    #TODO

    # widget placements using layout manager (Grid is most likely candidate since our window isn't resizeable anyways)

    leftColPaddingX = 25
    PaddingY = 20
    rightColPaddingX = 10
    
    batteryLabel.grid(row=0, column=0, ipadx=leftColPaddingX, ipady=PaddingY, sticky="w")
    batteryPercentageLabel.grid(row=0, column=1, ipadx=rightColPaddingX, ipady=PaddingY)
    
    altitudeLabel.grid(row=1, column=0, ipadx=leftColPaddingX, ipady=PaddingY, sticky="w")
    altitudeValueLabel.grid(row=1, column=1, ipadx=rightColPaddingX, ipady=PaddingY)
    
    speedLabel.grid(row=2, column=0, ipadx=leftColPaddingX, ipady=PaddingY, sticky="w")
    speedValueLabel.grid(row=2, column=1, ipadx=rightColPaddingX, ipady=PaddingY)
    

    innerDataFrame.pack(padx=(2, 2), pady=(2,2), anchor="center")
    emergencyButton.pack(ipadx=leftColPaddingX, ipady=10)
    outerDataFrame.pack(ipady=10, ipadx=10)
    


    
    win.mainloop()                  # keeps the window looping

main()