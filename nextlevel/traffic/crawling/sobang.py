from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")


def testfn(img):
    pass


def crawling_img(name):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element('name', 'q')
    elem.send_keys(name)
    elem.send_keys(Keys.RETURN)

    #
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")  # 브라우저의 높이를 자바스크립트로 찾음
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 브라우저 끝까지 스크롤을 내림
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element(By.CSS_SELECTOR,".mye4qd").click()
            except:
                break
        last_height = new_height

    imgs = driver.find_elements(By.CSS_SELECTOR,".rg_i.Q4LuWd")
    print(type(imgs))
    dir = ".\car" + "\\" + name

    createDirectory(dir) #폴더 생성
    count = 1


    for img in imgs:
        try:
            img.click()
            #print("a")
            time.sleep(2)

            imgUrl = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")

            #print(imgUrl)
            #경로
            path = "C:\\projects\\nextlevel\\traffic\\crawling\\car\\" + name +"\\"
            urllib.request.urlretrieve(imgUrl, path + name + str(count) + ".jpg")

            count = count + 1
            #print(count)
            #개수변경
            if count >=100:
                break
        except:
            pass
    driver.close()

idols = ["소방차", "진화용 소방차", "소방차 종류", "119"]

for idol in idols:
    crawling_img(idol)

