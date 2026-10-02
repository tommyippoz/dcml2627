import time
import psutil
import datetime

####################################################################################
# TASK: Write a monitor to detect if someone is starting off new applications
####################################################################################

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    arr_result = psutil.cpu_times(percpu=True)
    print("The amount of virtual cpus is " + str(len(arr_result)))
    old_mem = None
    old_cpu = None
    old_n_proc = None
    while True:
        # Reading current data
        avail_memory = psutil.virtual_memory().available
        cpu_usage = psutil.cpu_percent()
        now = datetime.datetime.now()
        number_processes = len(psutil.pids())

        # RULE TO UNDERSTAND IS A NEW APP WAS OPENED
        if old_cpu is not None:
            if old_n_proc < number_processes:
                print(str(now) + " - NEW APPLICATION HAS BEEN OPENED")
        print("memory: " + str(avail_memory) + " cpu_usage: " + str(cpu_usage))

        # Current data becomes old data
        old_mem = avail_memory
        old_cpu = cpu_usage
        old_n_proc = number_processes

        # Sleep 1 second
        time.sleep(1)

