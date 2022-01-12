from pynput.keyboard import Key, Controller

keyboard = Controller()
key = "a"

keyboard.press(key)
keyboard.release(key)