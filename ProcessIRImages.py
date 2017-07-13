import os

import matplotlib.pyplot as plt
from numpy import *


from ImageAnalyzer import ImageAnalyzer

'''
Moves to the directory where the images are.
Calls the function to process the image
Prints a report to the reports directory.
'''

# counter for the amount of files in the directory
counter = 0

# lists to hold the x and y values for each image
x_values = []
y_values = []

# initializing the temp variables
temp_path = ""
temp_analyzer = None

# initializing the chart
plt.title("IR Images")
plt.xlabel("Image Number (Representative of Altitude)")
plt.ylabel("Lightness Value")

# getting the current directory and setting it to the folder with images
scripts_directory = os.getcwd()
ir_images_directory = scripts_directory.replace("/scripts", "/images/ir_images")
#ir_images_directory = "/Users/stoudenmiersh/OneDrive/DCIM/IR_Photos"
reports_directory = scripts_directory.replace("/scripts", "/reports")

outfile = open(reports_directory + "/ir_images.csv", 'w')

# looping through every image in the folder containing the images
for root, dirs, files in os.walk(ir_images_directory):
    if(len(dirs) == 0):
        temp_path = root
    for root2, dirs2, files2 in os.walk(temp_path):
        for f in files2:
            #counter+=1
            if (f[-3:].lower() == "jpg"):
            #if (f[-3:].lower() == "jpg" and counter % 10  == 0):   # only detects the file if it is a .jpg
                temp_analyzer = ImageAnalyzer(root2+"/"+f)
                x_values.append(counter)
                image_width = temp_analyzer.getImageWidth()
                image_height = temp_analyzer.getImageHeight()
                temp_analyzer.cropImage(int((7/16.0)*image_width), 0,
                                        int((9/16.0)*image_width), int((1/8.0)*image_height))
                y_values.append(temp_analyzer.getImageHls()[1])
                outfile.write(str(counter) + "," + str(temp_analyzer.getImageHls()[1]) + "\n")
                counter+=1
                print(str(counter) + "   " + root2+"/"+f + "         "+str(temp_analyzer.getImageHls()[1]))

    #plt.plot(x_values,y_values)

# Use polyfit.
#best_fit = polyfit(x_values, y_values, 3)
#polynomial = poly1d(best_fit)

#plt.plt(x_values, poly1d(polyfit(x_values, y_values, 3))(x_values))
#plt.plot(x_values,y_values, "yo", x_values, polynomial(x_values), "--k")

outfile.close()

plt.plot(x_values, y_values)
plt.show()

print("Image count:",counter)
