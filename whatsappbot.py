from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


with open('about.txt', 'r',encoding='utf-8') as about:
    aboutlist = list()
    text = about.read()
    aboutlist = text.split('\n')
    a = len(aboutlist)
    aboutlist_len = a - 1

def start():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get('https://web.whatsapp.com/')
    input('Press any letter and enter for start \n')
    print(f'starting with {aboutlist_len} element')
    sleep(3)
    i = 0
    x = 0
    v = 0
    message_area = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/div[4]/div[2]/div[1]/div/div[2]')
    while True:
        x = 0
        for x in range(aboutlist_len):
            duzenle = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/div[4]/div[2]/div[1]/span[2]/div')
            duzenle.click()
            for i in range(11):
                message_area.send_keys(Keys.BACK_SPACE)
            oText = aboutlist[x]
            message_area.send_keys(oText)
            message_area.send_keys(Keys.ENTER)
            print('Changed to:',oText)
            sleep(7)
start()