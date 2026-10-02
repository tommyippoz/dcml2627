import time

import psutil

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    arr_result = psutil.cpu_times(percpu=True)
    print("The amount of virtual cpus is " + str(len(arr_result)))

    for i in range(10):

        # Reads data via the psutil library (has to be downloaded and imported)
        arr_result = psutil.net_connections()

        # Prints array lentgh to video
        print(len(arr_result))

        # Sleep for 1 second
        time.sleep(1)

