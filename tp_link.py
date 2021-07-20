from selenium import webdriver
from getpass import getpass
import time

username = "admin"
# input("Enter in your username: ")
password = getpass("Enter your password: ")

driver = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
driver.get("http://192.168.0.1/")

username_textbox = driver.find_element_by_id("userName")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("pcPassword")
password_textbox.send_keys(password)

login_button = driver.find_element_by_id("loginBtn")
login_button.click()

driver.switch_to.frame("mainFrame")
disconnect_button = driver.find_element_by_id("Disconnect")
disconnect_button.click()
time.sleep(10)
connect_button = driver.find_element_by_id("Connect")
connect_button.click()
time.sleep(1)
driver.close()
driver.quit()