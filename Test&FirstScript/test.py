import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\User\\Desktop\\\לימודים\\פרויקט גמר\\selenium\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.implicitly_wait(5)

######## LOGIN #########
driver.get('https://he.wikipedia.org/w/index.php?title=%D7%9E%D7%99%D7%95%D7%97%D7%93:%D7%9B%D7%A0%D7%99%D7%A1%D7%94_%D7%9C%D7%97%D7%A9%D7%91%D7%95%D7%9F&returnto=%D7%A2%D7%9E%D7%95%D7%93+%D7%A8%D7%90%D7%A9%D7%99')
username = driver.find_element(By.ID, 'wpName1')
username.send_keys("Alonzimmer")
password = driver.find_element(By.ID, 'wpPassword1')
password.send_keys('ASD123456ASD')
login = driver.find_element(By.ID, 'wpLoginAttempt')
login.click()

######### Random - Page ##################
search = driver.find_element(By.XPATH, '//a[@href="/wiki/%D7%9E%D7%99%D7%95%D7%97%D7%93:%D7%90%D7%A7%D7%A8%D7%90%D7%99"]')
search.click()


######### Add - Tool ##################
search = driver.find_element(By.XPATH, '//div[@class="mw-sidebar"]//div[@class="vector-menu-content"]//li[@class="mw-list-item mw-list-item-js"]//a[@href="#"]')
search.click()

expected = 'בוצע'
actual = driver.find_element(By.ID, "label-done").text
assert actual == expected

#time.sleep(2)

search = driver.find_element(By.ID, "checkBox")

before = search.get_attribute("checked")
assert not before

search.click()

after = search.get_attribute("checked")
assert after

current = driver.current_url


search = driver.find_element(By.XPATH, '//a[@href="/wiki/%D7%9E%D7%99%D7%95%D7%97%D7%93:%D7%90%D7%A7%D7%A8%D7%90%D7%99"]')
search.click()

#time.sleep(2)

driver.get(current)

search = driver.find_element(By.XPATH, '//div[@class="mw-sidebar"]//div[@class="vector-menu-content"]//li[@class="mw-list-item mw-list-item-js"]//a[@href="#"]')
search.click()

search = driver.find_element(By.ID, "checkBox")

checked = search.get_attribute("checked")
# assert after == checked

#time.sleep(4)

######### Category - Page ###########

category = driver.find_element(By.XPATH, '//div[@class="catlinks"]//ul/li')
category.click()


search = driver.find_element(By.XPATH,'//div[@class="mw-sidebar"]//div[@class="vector-menu-content"]//li[@class="mw-list-item mw-list-item-js"]//a[@href="#"]')
search.click()


try:
    search = driver.find_element(By.ID, "checkBox")
    search.click()
except:
    print("Check Box not exist!")

text = driver.find_element(By.XPATH, '//h1[@class="firstHeading"]//p').text
print(text)

expected = '[ (%xx) 1/n ]'
assert text == expected

expected = '[ 1/m ]'
try:
    text = driver.find_element(By.XPATH, '//div[@id="mw-subcategories"]//div//ul/li/p').text
    assert expected == text
    print(text)
except:
    print('No sub-categories in this category page!')
















