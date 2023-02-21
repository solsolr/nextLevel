import cv2


def ts():
    img_src = cv2.imread("./img/st0.jpg")
    img = cv2.resize(img_src, dsize=(0, 0), fx=0.1, fy=0.1, interpolation=cv2.INTER_LINEAR)

    winname = "test"
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)   # create a named window
    #cv2.setWindowProperty(winname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.moveWindow(winname, 0, 0)   # Move it to (40, 30)
    cv2.imshow(winname, img)
    cv2.resizeWindow(winname, 270, 5)  
    cv2.waitKey()
    cv2.destroyAllWindows()


ts()