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
chrome.find_element(By.LINK_TEXT,"Contul meu").click()
email_input = chrome.find_element(By.ID,"email")
email_input.send_keys("aaasdfsdfd@yahoo.com")
chrome.find_element(By.ID,"passwd").send_keys("Assssla")
chrome.find_element(By.ID,"SubmitLogin").click()
assert chrome.find_element(By.XPATH,"//*[@id='center_column']/div[1]") == "Am întâmpinat 1 problemă:"
