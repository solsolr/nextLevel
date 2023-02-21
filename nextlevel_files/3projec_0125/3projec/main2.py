import cv2



src = cv2.imread("img/1.png", cv2.IMREAD_COLOR)

dst = cv2.resize(src, dsize=(100, 50), interpolation=cv2.INTER_AREA)
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)
#del title


cv2.namedWindow('src',cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('src', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()