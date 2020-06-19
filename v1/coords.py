from pynput import mouse

# helps getget mouse coordinates to know how to take screenshot
def on_click(x, y, button, pressed):
    if pressed:
        print(x, y)


# Collect events until released
with mouse.Listener(
        on_click=on_click) as listener:
    listener.join()
