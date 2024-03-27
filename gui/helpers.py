import customtkinter as ctk

def createNiceFrame(root: ctk.CTk, x=800, y=400) -> tuple[ctk.CTkFrame, ctk.CTkFrame]:
    '''
    ## Function
        returns a more appropriate frame, consisting of an inner and outter frame.
        Only the inner frame should house other widgets such as labels and buttons.

    ## Parameters
        `root`: ctk.CTk
            Represents the main/root window to place your frame.
        `x`: int
            Represents the horizontal size of the frames.
        `y`: int
            Represents the vertical size of the frames.
    
    ## Returns
        `tuple(ctk.CTkFrame, ctk.CTkFrame)`
            Returns a tuple containing both the inner and outter frames which can be
            used to add widgets. Sample usage:

            ```python
            win = ctk.CTk()
            innerFrame, outterFrame = createNiceFrame(win)
            ```
    '''

    outerDataFrame = ctk.CTkFrame(root,
                             width=x,
                             height=y)
    innerDataFrame = ctk.CTkFrame(outerDataFrame,
                             width=x,
                             height=y,
                             border_width=0)
    
    innerDataFrame.pack(padx=(2, 2), pady=(10,5), anchor="center")

    return (innerDataFrame, outerDataFrame)