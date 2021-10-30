from selenium import webdriver
from time import sleep

browser = webdriver.Firefox(executable_path=r'C:\Users\valex\Downloads\geckodriver-v0.30.0-win64\geckodriver.exe')
browser.get('https://github.com')
browser.maximize_window()
sleep(10 )
browser.quit()
