from selenium import webdriver
import pyautogui as pKHOIR
import time as t 





khoir = webdriver.Chrome('chromedriver')
url = 'http://m.facebook.com/'
khoir.get(url)

password = open('password.txt', 'r')
khoir.find_element_by_id('m_login_email').send_keys('khoir359')
khoir.find_element_by_id('m_login_password').send_keys(password.read())
khoir.find_element_by_id('u_0_5').click()
t.sleep(2)
khoir.get(url+'abeka.pratamaa.77')

khoir.find_element_by_css_selector('#u_0_13 > a').click()
t.sleep(1)
khoir.find_element_by_css_selector('#root > div._544l._7a_1._55i2.accelerate > div > div > div._5c0f > a:nth-child(4)').click()
t.sleep(1)
khoir.find_element_by_css_selector('#tag_profile_something_else').click()
# pKHOIR.click()
print(pKHOIR.position())
pKHOIR.typewrite(['enter'])
