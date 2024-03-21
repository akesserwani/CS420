import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Frame Border Padding Example")

    # Create an outer frame with padding
    outer_frame = tk.Frame(root, bg="gray", padx=10, pady=10)
    outer_frame.grid(row=0, column=0)

    # Create an inner frame
    inner_frame = tk.Frame(outer_frame, bg="lightblue", width=300, height=200)
    inner_frame.grid(row=0, column=0)

    # Adding some widgets inside the inner frame
    label = tk.Label(inner_frame, text="This is a frame with border padding")
    label.grid(row=0, column=0, padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()