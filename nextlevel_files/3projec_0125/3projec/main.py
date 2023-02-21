import sys
import glob
import cv2

# images에 있는 모든 jpg,png 파일을 img_files 리스트에 추가
img_files = glob.glob('.\\img\\*.jpg')
img_files = glob.glob('.\\img\\*stop.png')
# 이미지 없을때 예외처리
if not img_files:
    print("jpg 이미지가 읎어요..")
    sys.exit()

# 전체화면으로  jinmi 창 생성
cv2.namedWindow('jinmi', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('jinmi', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# 슬라이드 쇼 반복을 위한 반복문
count = len(img_files)
index = 0

while True:
    img = cv2.imread(img_files[index])
    # 예외처리
    if img is None:
        print("이미지를 불러오는데 실패했습니다.")
        break

    # ESC가 입력되면 break
    cv2.imshow('jinmi', img)
    if cv2.waitKey(3000) == 27:
        break

    # index가 이미지 리스트보다 커지거나 같아지면 다시 0으로
    index += 1
    if index >= count:
        index = 0

cv2.destroyAllWindows()
