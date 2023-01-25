from time import sleep

import elements as elements
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys



chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://cafeo.ro/")
chrome.find_element(By.CSS_SELECTOR,"[class='li_login last']").click()
chrome.find_element(By.CLASS_NAME,"submit").submit()
assert chrome.find_element(By.CSS_SELECTOR,"[ol>li]")=="Adresa de e-mail este invalida"
sleep(10)