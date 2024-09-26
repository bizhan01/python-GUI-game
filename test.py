import tkinter as tk

def move_forward():
    print("Moving forward")

def move_backward():
    print("Moving backward")

def turn_left():
    print("Turning left")

def turn_right():
    print("Turning right")

# Create the main window
window = tk.Tk()
window.title("Robot Control")

# Create buttons for robot control
forward_button = tk.Button(window, text="Forward", command=move_forward)
forward_button.pack()

backward_button = tk.Button(window, text="Backward", command=move_backward)
backward_button.pack()

left_button = tk.Button(window, text="Left", command=turn_left)
left_button.pack()

right_button = tk.Button(window, text="Right", command=turn_right)
right_button.pack()

# Start the GUI event loop
window.mainloop()