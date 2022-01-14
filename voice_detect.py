#coding = utf-8
#sudo apt-get install chromium-chromedriver
from selenium import webdriver  
from selenium.webdriver.support.ui import Select
import time
import os
import requests
#Fs81Kd

#真的是棒到不行耶
#好棒!!
#這個版本就加個註解而已拉
#Linux版本  請下載對應版本的chrome driver 放在/usr/bin/路徑 
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'

options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")     #不顯示受自動軟體控制
options.add_argument("--window-size=800,600")  #設定窗大小
#後來發現無頭模式會無法偵測麥克風訊號
#options.add_argument('--headless')             #無頭模式 不顯示chrome視窗在背景爬蟲 
options.add_argument('--disable-gpu')          #關閉Chrome GPU加速

#賦予chrome driver 麥克風,鏡頭,位置,通知 權限
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,     # 1:allow, 2:block 
    "profile.default_content_setting_values.media_stream_camera": 1,  # 1:allow, 2:block 
    "profile.default_content_setting_values.geolocation": 1,          # 1:allow, 2:block 
    "profile.default_content_setting_values.notifications": 1         # 1:allow, 2:block 
  })

driver = webdriver.Chrome(executable_path = CHROMEDRIVER_PATH,chrome_options=options)

#driver = webdriver.Chrome()

driver.get("https://translate.google.com.tw/?hl=zh-TW&tab=wT&sl=zh-CN&tl=zh-TW&op=translate")

#buffer1 ='//div[@class="d-flex flex-wrap"]/div[4]/div[2]'
buffer1 ='//button[@jsname="Sz6qce"]'
item = driver.find_element_by_xpath(buffer1).click()

#driver.get(driver.current_url)
#print(driver.current_url)
def do_light_change():
    r = requests.get("http://0.0.0.0:80/submit")
    try:
        Listen_Restart()                
    except:
        print('some err 2')

def Listen_Restart():
    
    
    driver.get("https://translate.google.com.tw/?hl=zh-TW&tab=wT&sl=zh-CN&tl=zh-TW&op=translate")
    buffer34 ='//button[@jsname="Sz6qce"]'
    item = driver.find_element_by_xpath(buffer34).click()
    global err_cnt
    err_cnt = 0

global err_cnt
err_cnt = 0

text_pre = ""
time_out_cnt = 0
while True:

    if err_cnt > 38:
        err_cnt = 0
        Listen_Restart()

    time.sleep(200/1000)
    try:
        buffer2 ='//span[@jsname="W297wb"]'
        item2 = driver.find_element_by_xpath(buffer2).text

        if(text_pre != item2):
            text_pre = item2
            time_out_cnt = 0
        elif(text_pre == item2):
            time_out_cnt+=1

            print(time_out_cnt)
            if(time_out_cnt >= 120):
                time_out_cnt = 0
                Listen_Restart()
            

        if "燈" in item2:
            do_light_change()
        elif "開關" in item2:     
            do_light_change()
        elif "打開電" in item2:         
            do_light_change()
        elif "關閉電" in item2:         
            do_light_change()

        print(item2)
        if(len(item2) > 50):
            print("too long clear")
            try:                
                Listen_Restart()
                # buffer3 ='//button[@jsname="X5DuWc"]'
                # item3 = driver.find_element_by_xpath(buffer3)
                # item3.click()
            except:                
                err_cnt+=1
                print('err '+ str(err_cnt))

    except:
        err_cnt+=1
        print('err '+ str(err_cnt))
        #print('some err')


os.system("pause") 
driver.close() 
