from djitellopy import Tello
import keyboard

tello = Tello()

tello.connect()
tello.takeoff()


while True:
    # Check if an arrow key is pressed
    if keyboard.is_pressed('a'):
        tello.move_left(50)
    elif keyboard.is_pressed('d'):
        tello.move_right(50)
    elif keyboard.is_pressed('w'):
        tello.move_up(50)
    elif keyboard.is_pressed('s'):
        tello.move_down(50)
    elif keyboard.is_pressed('space'):
        tello.land()
        break



