from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep 
from random import randint

chromedriver_path = '/home/rusty/devv/selium/chromedriver/chromedriver'  # chromedriver path
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.google.com')
sleep(1)

username = webdriver.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
username.send_keys('ajul maharjan')
sleep(1)

buttonSearch = webdriver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.FPdoLc.tfB0Bf > center > input.gNO89b')
buttonSearch.click()
print("button clicked!!")

sleep(randint(4,6))
search = webdriver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3')
search.click()
print('linkedin')
sleep(randint(5,9))

biolink = webdriver.find_element_by_xpath('/html/body/main/section[1]/section/section[1]/div/div[1]/div[2]/div/div[2]/a')
biolink.click()
print('bio page!!')
sleep(3)

button = webdriver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/p/a[5]/button')
button.click()
print('light-dark')
sleep(3)


buttonSearch = webdriver.find_element_by_css_selector('#box > button.btn.btn-dark')
print("switched - dark")
buttonSearch.click()
sleep(randint(4,7))


buttonSearch = webdriver.find_element_by_css_selector('/#box > button.btn.btn-light')
print("switched - light")
buttonSearch.click()
sleep(randint(2,7))