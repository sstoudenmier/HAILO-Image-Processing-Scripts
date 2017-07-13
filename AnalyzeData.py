from os import getcwd

import matplotlib.pyplot as plt
from numpy import *

TIME_POSITION = 0
LUX_POSITION = 7
IR_POSITION = 4
HUMIDITY_POSITION = 10

curr_dir = getcwd()
data_dir = curr_dir.replace("/scripts","/data")

infile = open(data_dir + "/Payload_2_4-12-16.CSV", 'r')

x_values = []
y_values = []

plt.title("IR")
plt.xlabel("Time (ms)")
plt.ylabel("IR")

counter = 0

for line in infile:
    temp = line.split(',')
    if counter > 0 and eval(temp[TIME_POSITION]) > 2160000:
        break
    if counter > 0 and temp != "\n":
        if eval(temp[IR_POSITION]) < 1000000000:
            x_values.append(eval(temp[TIME_POSITION]))
            y_values.append(eval(temp[HUMIDITY_POSITION]))
    counter+=1

infile.close()

plt.plot(x_values, y_values)
plt.show()
