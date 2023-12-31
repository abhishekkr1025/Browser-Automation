from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
options = Options()
options.add_experimental_option("detach",True)


browser = webdriver.Chrome()
browser.get("https://www.twitter.com")
time.sleep(2)
login = browser.find_elements_by_xpath('//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[3]')
  
# using the click function which is similar to a click in the mouse.
login[0].click()
  
print("Login in Twitter")
  
user = browser.find_elements_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[1]/input')
  
# Enter User Name
user[0].send_keys('USER-NAME')
  
user = browser.find_element_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input')
  
# Reads password from a text file because
# saving the password in a script is just silly.
with open('test.txt', 'r') as myfile:  
    Password = myfile.read().replace('\n', '')
user.send_keys(Password)
  
LOG = browser.find_elements_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/input[1]')
LOG[0].click()
print("Login Successful")
time.sleep(5)
  
elem = browser.find_element_by_name("q")
elem.click()
elem.clear()
  
elem.send_keys("Geeks for geeks ")
  
# using keys to send special KEYS 
elem.send_keys(Keys.RETURN) 
  
print("Search Successful")
  
# closing the browser
browser.close() 

