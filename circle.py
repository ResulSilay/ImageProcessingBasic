from PIL import Image
from skimage import data, img_as_float,io
import numpy as np

def drawCircle(pixel_values,xc, yc, x, y): 
    pixel_values[xc+x][yc+y] = 0

def circle(xc, yc, r,pixel_values):
    x = 0
    y = r
    d = 3 - 2 * r 
    drawCircle(pixel_values,xc, yc, x, y)
    while (y >= x):
        x-=1
        if (d > 0):
            y-=1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6; 
        
        drawCircle(pixel_values,xc, yc, x, y)
        
        

xc = 50
yc = 50
r = 30
image = io.imread("image.png")
row,col,ch = image.shape
pixel_values = np.copy(image)
print(pixel_values)
circle(xc, yc, r,pixel_values)