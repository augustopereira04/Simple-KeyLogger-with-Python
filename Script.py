from pynput.keyboard import Key, Listener

def keyPress(key):
    print(f"{key} pressed")

def keyRealease(key):
    if key == Key.esc:
        return False 
    
with Listener (on_press=keyPress, on_release=keyRealease) as listener:
    listener.join()