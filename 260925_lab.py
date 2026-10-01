import time

import psutil

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    arr_result = psutil.cpu_times(percpu=True)
    print("The amount of virtual cpus is " + str(len(arr_result)))

    for i in range(10):
        arr_result = psutil.net_connections()
        print(len(arr_result))
        time.sleep(1)

