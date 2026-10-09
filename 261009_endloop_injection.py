import datetime
import random

# Script to perform error injection
if __name__ == '__main__':

    my_list = []
    print(datetime.datetime.now())
    while True:
        my_list.append(random.random())

