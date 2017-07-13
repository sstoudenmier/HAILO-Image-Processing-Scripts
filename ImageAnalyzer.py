from PIL import Image
from PIL import ImageStat

import colorsys

class ImageAnalyzer:

    # constructor for the ImageAnalyzer
    # imagePath - the file path for the image

    def __init__(self, imagePath):
        self.image = Image.open(imagePath)      # initializing the image
        self.height = self.image.height         # getting the height of the image
        self.width = self.image.width           # getting the width of the image
        self.stat = ImageStat.Stat(self.image)  # initializing the stats of an image

    # crops the image object contained in the analyze_image object
    # left, top, right, bottom - the boundaries at which to crop the image
    #                            in order to analyze it
    def cropImage(self, left, top, right, bottom):
        self.image = self.image.crop((left, top, right, bottom))
        self.height = self.image.height
        self.width = self.image.width
        self.stat = ImageStat.Stat(self.image)

    # returns an average of all RGB (red, green, blue) values for every pixel
    # in an image; return value is a list such that [R, G, B]
    def getImageRgb(self):
        temp = []
        pixelCount = self.stat.count[0]
        for val in self.stat.sum:
            temp.append(val / pixelCount)
        return temp

    # returns a average of all HLS (hue, lightness, saturation) values for every
    # pixel in an image; return value is a list such that [H, L, S]
    def getImageHls(self):
        temp = self.getImageRgb()
        return colorsys.rgb_to_hls(temp[0], temp[1], temp[2])

    # returns the maximum values for RGB such that:
    # (maxR, maxG, maxB)
    def getMaxRgb(self):
        temp = self.image.getextrema()
        return (temp[0][1], temp[1][1], temp[2][1])

    # returns the RGB(red, green, blue) values for a specific pixel in the image;
    # return values are formatted such that [red, green, blue] with values
    # ranging from 0 to 250 for each color
    def getPixelRgb(self, x, y):
        return self.image.getpixel((x,y))

    # returns the HLS (hue, lightness, saturation) values for a specific pixel
    # in the image; return value ranges from 0 (dark) to 250 (bright)
    def getPixelHls(self, x, y):
        temp = self.getPixelRgb(x,y)
        return colorsys.rgb_to_hls(temp[0], temp[1], temp[2])

    # returns the total count of pixels in an image
    def getPixelCount(self):
        return self.stat.count[0]

    # returns the width of the image
    def getImageWidth(self):
        return self.width

    # returns the height of the image
    def getImageHeight(self):
        return self.height
