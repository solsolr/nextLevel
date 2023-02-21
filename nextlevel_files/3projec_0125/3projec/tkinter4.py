import numpy as np
import glob
import cv2
sc=2
def sinho(work,sc=1) :
    if work == "재난" :

        # 원본 이미지
        #내림차순 sorted()
        src = glob.glob('.\\img\\wind*.jpg')

        #파일 유무 체크
        # for f in src:
        #     print(f)

    src = glob.glob('.\\img\\st*.jpg')
    print(src)
    cnt = len(src)
    #
    if sc > cnt:
        sc = cnt-1
    print(sc)


    # 무한 루프 실행

    idx = sc
    gin=0

    while True:

        img = cv2.imread(src[idx])

        if img is None: # 이미지가 없는 경우
            print('이미지없음')
            break
        resize_img = cv2.resize(img, dsize=(0, 0), fx=0.12, fy=0.1, interpolation=cv2.INTER_AREA)
        height, width = img.shape[:2]
        # 가로 ,세로
        mat = np.float32([[1, 0, 0], [0, 1, -15]])
        tran = cv2.warpAffine(resize_img, mat, (width, height))

        cv2.namedWindow('tran', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('tran', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        cv2.imshow("tran", tran)
        if cv2.waitKey(1000) >= 0: # 1초 동안 사진보여주는데 만약에 키보드 입력이 있으면 종료
            break

        # 사진을 다 보면 첫번째 사진으로 돌아감
        idx -= 1
        if idx < 0:
            idx = sc

        #긴급 신호를 받았을시에
        if gin==1 :
            if idx<=3 :
                idx+=5

    cv2.destroyAllWindows()


sinho("ㅇㅇ",20)









