import cv
import sys 
from pylab import *
#class ETMouse():    
 #   def setMousePosition(self, x, y):
  #      print [x,y]


#    Convert image to HSV and threshold to produced binary image based on Hue value.
def thresholdImage(img):
    #allocate temp image based on size of input img
    img_hsv = cv.CreateImage((img.width,img.height),8,3)   #3 channel
    img_thresh = cv.CreateImage((img.width,img.height),8,1)#1 channel

    cv.CvtColor(img, img_hsv, cv.CV_BGR2HSV)    
    #cv.InRangeS(img_hsv, cv.Scalar(100,5,5), cv.Scalar(255,40,40), img_thresh);
    cv.InRangeS(img_hsv, cv.Scalar(90,84,69), cv.Scalar(120,255,255), img_thresh);
    return(img_thresh)


    
#    Filter noisy pixels using custom kernel size. 
#    Removes visually insignificant noise such as speckles
def erodeImage(img):
    kernel = cv.CreateStructuringElementEx(9,9,5,5, cv.CV_SHAPE_CROSS) 
    # Erode- replaces pixel value with lowest value pixel in kernel
    cv.Erode(img,img,kernel,2)
    # Dilate- replaces pixel value with highest value pixel in kernel
    cv.Dilate(img,img,kernel,2)
    return img
    
def contour_iterator(contour):
    while contour:
        yield contour
        contour = contour.h_next()
                        
    
def findImageContour(img,frame):
    storage = cv.CreateMemStorage()
    cont = cv.FindContours(img, storage,cv.CV_RETR_EXTERNAL,cv.CV_CHAIN_APPROX_NONE,(0, 0))
    max_center = [None,0]
    for c in contour_iterator(cont):
    # Number of points must be more than or equal to 6 for cv.FitEllipse2
    # Use to set minimum size of object to be tracked.
        print "yaaaaaaaaaaaaaaaaaaaaa"
        if len(c) >= 1:  #60
            # Copy the contour into an array of (x,y)s
            PointArray2D32f = cv.CreateMat(1, len(c), cv.CV_32FC2)
            for (i, (x, y)) in enumerate(c):
                PointArray2D32f[0, i] = (x, y)
                # Fits ellipse to current contour.
                (center, size, angle) = cv.FitEllipse2(PointArray2D32f)
                # Only consider location of biggest contour  -- adapt for multiple object tracking
            #if size > max_center[1]:
            if(1):
                max_center[0] = center
                max_center[1] = size
                angle = angle
                        
            #if True:
                # Draw the current contour in gray
            #    gray = cv.CV_RGB(255, 255, 255)
            #    cv.DrawContours(img, c, gray, gray,0,1,8,(0,0))
                        
    if max_center[1] > 0:
        
		
		# Convert ellipse data from float to integer representation.
        print max_center
        center = (cv.Round(max_center[0][0]), cv.Round(max_center[0][1]))
        size = (cv.Round(max_center[1][0] * 0.5), cv.Round(max_center[1][1] * 0.5))
        color = cv.CV_RGB(255,0,0)
        
        #cv.Ellipse(frame, center, size,angle, 0, 360,color, 3, cv.CV_AA, 0)
        #return [2.6*max_center[0][0]-150, 2*max_center[0][1]-100]
        print max_center[0]
        return max_center[0]
    else: return[0,0]
def process(imag):
	cv.Flip(imag, imag,1)
	img = thresholdImage(imag)
	img = erodeImage(img)
	f=findImageContour(img,imag)
	print f
	return [int(f[0]),int(f[1])]
            