import os

import matplotlib.pyplot as plt
from numpy import *

from ImageAnalyzer import ImageAnalyzer


# counter for the amount of files in the directory
counter = 0

# lists to hold the x and y values for each image
full_brightness = []
ir_brightness = []
visible_brightness = []
ratio_values = []
image_number_ir = []
image_number_full = []

# initializing the temp variables
temp_path = ""
temp_analyzer = None

# initializing the chart
plt.title("Visible Brightness")
plt.xlabel("Image Position (Representative of Altitude)")
plt.ylabel("Brightness")

# getting the current directory and setting it to the folder with images
scripts_directory = os.getcwd()
ir_images_directory = scripts_directory.replace("/scripts", "/images/IR")
regular_images_directory = scripts_directory.replace("/scripts", "/images/Regular")
reports_directory = scripts_directory.replace("/scripts", "/reports")

outfile = open(reports_directory + "/ir_images.csv", 'w')

# looping through every image in the folder containing IR images
for root, dirs, files in os.walk(ir_images_directory):
    for f in files:
        #counter+=1
        if (f[-3:].lower() == "jpg"):
        #if (f[-3:].lower() == "jpg" and counter % 10  == 0):   # only detects the file if it is a .jpg
            temp_analyzer = ImageAnalyzer(root+"/"+f)
            image_number_ir.append(counter)
            image_width = temp_analyzer.getImageWidth()
            image_height = temp_analyzer.getImageHeight()
            temp_analyzer.cropImage(int((7/16.0)*image_width), int((7/16.0)*image_height),
                                    int((9/16.0)*image_width), int((9/16.0)*image_height))
            ir_brightness.append(temp_analyzer.getImageHls()[1])
            #outfile.write(str(counter) + "," + str(temp_analyzer.getImageHls()[1]) + "\n")
            counter+=1
            print(str(counter) + "   " + root+"/"+f + "         "+str(temp_analyzer.getImageHls()[1]))

counter = 0

# looping through every image in the folder containing Regular images
for root, dirs, files in os.walk(regular_images_directory):
    for f in files:
        #counter+=1
        if (f[-3:].lower() == "jpg"):
        #if (f[-3:].lower() == "jpg" and counter % 10  == 0):   # only detects the file if it is a .jpg
            temp_analyzer = ImageAnalyzer(root+"/"+f)
            image_number_full.append(counter)
            image_width = temp_analyzer.getImageWidth()
            image_height = temp_analyzer.getImageHeight()
            temp_analyzer.cropImage(int((7/16.0)*image_width), int((7/16.0)*image_height),
                                    int((9/16.0)*image_width), int((9/16.0)*image_height))
            full_brightness.append(temp_analyzer.getImageHls()[1])
            #outfile.write(str(counter) + "," + str(temp_analyzer.getImageHls()[1]) + "\n")
            counter+=1
            print(str(counter) + "   " + root+"/"+f + "         "+str(temp_analyzer.getImageHls()[1]))

for i in range(len(image_number_ir)):
    visible_brightness.append(full_brightness[i] - ir_brightness[i])
    ratio_values.append(ir_brightness[i] / visible_brightness[i])

outfile.write("Image Number, Full Brightness, IR Brightness, Visible Brightness\n")
for i in range(len(image_number_ir)):
    outfile.write(str(i) + "," + str(full_brightness[i]) + "," + str(ir_brightness[i]) + "," + str(visible_brightness[i]) + "\n")

outfile.close()

plt.plot(image_number_ir, visible_brightness)
plt.show()
