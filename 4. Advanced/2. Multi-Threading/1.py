#What is multi-threading?
#Multi-threading is a technique that allows a program to perform multiple tasks simultaneously.

#what is Task?
#Task is a process that is executed by a thread.

import time 
import threading

def number():
    for i in range(1,5):
        print(i)
        time.sleep(1)



def print_letters():
    for i in range(5):
        print(chr(ord('a') + i))
        time.sleep(1)


#create Thread
t1 = threading.Thread(target=number)
t2 = threading.Thread(target=print_letters)

#start Thread
t1.start()  
t2.start()
print(f"Is thread is alive? {t1.is_alive()}")
t1.join()
t2.join()

print("Done")

print(f"Is thread is alive? {t1.is_alive()}")