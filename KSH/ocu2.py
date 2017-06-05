from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
import time
import threading

count = 0
def start_timer(count) :
    count+=1
    print(count)
    timer = threading.Timer(1,start_timer,args=[count])
    timer.start()
    if count == 5:
        print('stop')
        timer.cancel()


driver = webdriver.Chrome(executable_path=r'chromedriver_win32/chromedriver')

driver.get('http://cons.ocu.ac.kr/')
keyboard = Controller()

frame = driver.find_element_by_name("main")
driver.switch_to_frame(frame)

f = open('login.txt','r')

login = driver.find_element_by_name("txtID")
login.send_keys(f.readline().split())
login = driver.find_element_by_name("txtPwd")
login.send_keys(f.readline())
login.submit()


selector = driver.find_element_by_name('SelSubject')

options = selector.find_elements_by_tag_name('option')
options = options[1:]

for option in range(0,len(options)):
    selectors = driver.find_element_by_name('SelSubject')

    optionss = selectors.find_elements_by_tag_name('option')
    optionss = optionss[1:]
    optionss[option].click()

    driver.find_element_by_link_text('본강의').click()

    td = driver.find_elements_by_tag_name('td')
    td = td[42: ]

    for i in range(0,8):
        td.pop()

    name_td = []
    chul_td = []

    for i in range(1,len(td),7) :
        name_td.append(td[i])

    for i in range(4,len(td),7) :
        chul_td.append(td[i])


    not_chul_suk = []
    for i in range(0,len(chul_td)) :
        if(chul_td[i].text == '미출석'):
            not_chul_suk.append(name_td[i])


    for item in not_chul_suk:
        item.click()
        time.sleep(1)
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        driver.switch_to_window(driver.window_handles[0])
        frame = driver.find_element_by_name("main")
        driver.switch_to_frame(frame)
        driver.find_elements_by_tag_name('img')[21].click()
        driver.switch_to_window(driver.window_handles[1])
        time.sleep(1)
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        driver.switch_to_window(driver.window_handles[0]) #메인
        frame = driver.find_element_by_name("main")
        driver.switch_to_frame(frame)
        driver.find_elements_by_tag_name('img')[22].click()
        time.sleep(2)
start_timer(0)
