import numpy as np
import glob
import cv2


# 원본 이미지
src = cv2.imread('img/1_re.png')
# cv2.imshow("org",src)



resize_img = cv2.resize(src, dsize=(0, 0), fx=0.12, fy=0.1, interpolation=cv2.INTER_AREA)
height, width = src.shape[:2]
#가로 ,세로
mat = np.float32([[1, 0, 0], [0, 1, -15]])
tran = cv2.warpAffine(resize_img, mat, (width,height))

cv2.namedWindow('tran',cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('tran', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cv2.imshow("tran", tran)

cv2.waitKey(0)


