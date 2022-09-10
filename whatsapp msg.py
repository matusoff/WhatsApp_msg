from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

browser = webdriver.Chrome(executable_path='C:\\webdrivers\chromedriver.exe')
browser.maximize_window()

browser.get('https://web.whatsapp.com/')

with open('groups.txt', 'r', encoding='utf-8') as f:
    groups = [group.strip() for group in f.readlines()]

with open('msg1.txt', 'r') as f:
    msg1 = f.read()


for group in groups:
    search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
    search_box = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, search_xpath))
    )
    

    time.sleep(1)

    pyperclip.copy(group)
    search_box.send_keys(Keys.CONTROL +"v")

    time.sleep(2)
    
    group_xpath = f'//span[@title="{group}"]'
    group_title = browser.find_element_by_xpath(group_xpath)

    group_title.click()

    time.sleep(1)

    input_xpath = '//div[@contenteditable="true"][@data-tab="9"]'
    input_box = browser.find_element_by_xpath(input_xpath)

    pyperclip.copy(msg1)
    input_box.send_keys(Keys.CONTROL +"v")

    input_box.send_keys(Keys.ENTER)

    time.sleep(2)



    



