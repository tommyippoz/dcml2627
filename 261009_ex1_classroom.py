import time
import psutil
import datetime

####################################################################################
# ASSIGNMENT: Write a monitor to detect if some task is running an endless loop
####################################################################################

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    old_mem_value = 0.0
    while True:
        # Reading useful data
        avail_memory = psutil.virtual_memory().available
        cpu_usage = psutil.cpu_percent()
        now = datetime.datetime.now()

        print("Time: " + str(now) + " Avail Mem: " + str(avail_memory) + " CPU%:" + str(cpu_usage))

        # RULE IO UNDERSTAND IF 1+ PROGRAMS ARE LOOPING
        # if memory drops a lot + cpu usage never below 14
        mem_threshold = old_mem_value*0.98
        if cpu_usage > 14.0 and avail_memory < mem_threshold:
            print("Endless Loop")

        old_mem_value = avail_memory
        # Sleep 1 second
        time.sleep(1)

