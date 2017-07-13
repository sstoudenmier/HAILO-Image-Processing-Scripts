import os
import sys
import webbrowser

import matplotlib.pyplot as plt

from analyze_image import ImageAnalyzer

'''
Moves to the directory where the images are.
Calls the function to process the image
Prints a report to the reports directory.
'''

# counter for the amount of files in the directory
counter = 0
badImageCounter = 0

# initializing the temp variables
temp_path = ""
temp_analyzer = None

# getting the current directory and setting it to the folder with images
scripts_directory = os.getcwd()
ir_images_directory = "/Users/stoudenmiersh/OneDrive/DCIM/IR_Photos"
regular_images_directory = "/Users/stoudenmiersh/OneDrive/DCIM/Regular_Photos"
reports_directory = scripts_directory.replace("/scripts", "/reports")

# checks to see if the image is bad and should be thrown out;
# returns true if it is bad; returns false otherwise
def isBad(analyzer):
    if( analyzer.getMaxRgb()[0] >= 255 and analyzer.getMaxRgb()[1] >= 255 and
        analyzer.getMaxRgb()[2] >= 255):
        return True
    return False

# looping through every image in the folder containing the images;
# if the image contains a pixel at the maximum pixel value it is assumed
# that there is part of the sun or solar flare in the image and the
# image is removed
for root, dirs, files in os.walk(regular_images_directory):
    if(len(dirs) == 0):
        temp_path = root
    for root2, dirs2, files2 in os.walk(temp_path):
        for f in files2:
            if (f[-3:].lower() == "jpg"):
            #if (f[-3:].lower() == "jpg" and counter % 100  == 0):   # only detects the file if it is a .jpg
                counter+=1
                print(ImageAnalyzer(root2+"/"+f).getMaxRgb(), end=" ")
                print(root2+"/"+f, end=" ")
                if (isBad(ImageAnalyzer(root2+"/"+f))):
                    print("is bad")
                    badImageCounter+=1
                    os.remove(root2+"/"+f)
                else:
                    print("is good")


print("Bad image count:",badImageCounter)
print("Image count:",counter)
