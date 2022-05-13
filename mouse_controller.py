from pynput.mouse import Button, Controller

mouse = Controller()

# Read pointer position
print(f'The current pointer position is {mouse.position}')

# Set pointer position
mouse.position = (1114, 487)
print(f'Now we have moved it to {mouse.position}')

# Move pointer relative to current position
mouse.move(dx=10, dy=-10)

# Press and release
mouse.press(Button.left)
mouse.release(Button.left)

# Double click; this is different from pressing and releasing
# twice on macOS
mouse.click(Button.left, 2)

# Scroll two steps down
mouse.scroll(0, 2)