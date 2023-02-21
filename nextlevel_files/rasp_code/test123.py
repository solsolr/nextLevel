import cv2
# from tkinter import *

# tk = Tk()

# canvas = Canvas(tk, width = 100, height = 100, bd = 0, highlightthickness = 0)

# canvas.pack()

img_src = cv2.imread("./img/man004.jpg")
img = cv2.resize(img_src, dsize=(0, 0), fx=0.7, fy=0.9, interpolation=cv2.INTER_LINEAR)

winname = "test"
cv2.namedWindow(winname, cv2.WINDOW_NORMAL)   # create a named window
cv2.setWindowProperty(winname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.moveWindow(winname, 0, 0)   # Move it to (40, 30)
cv2.imshow(winname, img)
cv2.resizeWindow(winname, 400, 50)  
cv2.waitKey()
cv2.destroyAllWindows()
# cvNamedWindow("Name", CV_WINDOW_NORMAL);
# cvSetWindowProperty("Name", CV_WND_PROP_FULLSCREEN, CV_WINDOW_FULLSCREEN); 
# cvShowImage("Name", your_image);