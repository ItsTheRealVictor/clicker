from selenium import webdriver
from time import sleep
import pyautogui as pag


jobLink = 'https://jobs.intel.com/page/show/search-results#t=Jobs&sort=relevancy&layout=table'

browser = webdriver.Firefox(executable_path=r'C:\Users\valex\Downloads\geckodriver-v0.30.0-win64\geckodriver.exe')
browser.get(jobLink)
browser.maximize_window()


sleep(10 )
browser.quit()


