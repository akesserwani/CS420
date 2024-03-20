import customtkinter as ctk

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

    # Create the active data frame to put on the west side of the main window
    dataFrame = ctk.CTkFrame(win,
                             width=200,
                             height=400)
    batteryLabel = ctk.CTkLabel(dataFrame)

    # Create the LED frame
    #TODO

    # Create the preprogrammed buttons frame
    #TODO

    # Create the controls frame on the east
    #TODO

    # Create active camera feed frame in the center
    #TODO

    # widget placements using layout manager (Grid is most likely candidate since our window isn't resizeable anyways)
    dataFrame.pack()
    batteryLabel.pack()



    
    win.mainloop()                  # keeps the window looping

main()