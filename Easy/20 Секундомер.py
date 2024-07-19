
import time
secs = 0
mins = 0
hrs = 0
def start_counting():
    global secs,mins,hrs
    while True:
        print(f'\r {hrs}:{mins}:{secs}',end='')
        secs += 1
        time.sleep(1)
        if secs == 60:
            mins += 1
            secs = 0
        if mins == 60:
            hrs += 1
            mins = 0
start_counting()