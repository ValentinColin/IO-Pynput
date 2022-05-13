import time

# Listener
from pynput import mouse
from pynput import keyboard

# Controller
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController


def type_humanly(string:str, time_char=0.05, time_line=1):
	lines = string.splitlines()
	for line in lines:
		for char in line:
			keyboard.tap(char)
			time.sleep(time_char)
		keyboard.tap(Key.enter)
		time.sleep(time_line)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()

mouse = MouseController()
keyboard = KeyboardController()


# set mouse position on SublimeText app
mouse.position = (40, 400)
mouse.click(Button.right) # équivalent avec press/release

time.sleep(1)

# set mouse position on SublimeText -> New Window
mouse.position = (170, 365)
mouse.click(Button.left) # équivalent avec press/release

time.sleep(2)

text = """\
Salut !
Comment vas-tu ?
A quelle heure veux-tu manger ?
"""

type_humanly(text)
