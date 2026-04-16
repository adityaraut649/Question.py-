import time 
import threading


def background_task():
    while True:
        print("Background Task")
        time.sleep(1)

# create a daemon thread 
thread = threading.Thread(target=background_task)

#Daemon Thread
thread.daemon = True 

thread.start()

#main program ends here
time.sleep(5)
print("Done")