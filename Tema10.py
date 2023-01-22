from time import sleep

import elements as elements
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


# #Test1
# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome.maximize_window()
# chrome.get("https://the-internet.herokuapp.com/login")
# text_welcome = chrome.find_element(By.TAG_NAME, "h2")
# assert text_welcome.text=="Login Page"
# assert chrome.find_element(By.TAG_NAME,"h4")
# chrome.quit()
# #Test2
# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome.maximize_window()
# chrome.get("https://the-internet.herokuapp.com/login")
# chrome.find_element(By.LINK_TEXT,"Elemental Selenium").click()
# chld = chrome.window_handles[1]
# chrome.switch_to.window(chld)
# assert chrome.current_url=='http://elementalselenium.com/'
# chrome.quit()
# #Test3
# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome.maximize_window()
# chrome.get("https://the-internet.herokuapp.com/login")
# username_input = chrome.find_element(By.ID,"username")
# username_input.send_keys("tomsmith")
# chrome.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
# chrome.find_element(By.CLASS_NAME,"radius").click()
# chrome.find_element(By.CSS_SELECTOR, "[href='/logout']").click()
# assert chrome.current_url=="https://the-internet.herokuapp.com/login"
# chrome.quit()
# #Test4
# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome.maximize_window()
# chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
# chrome.find_element(By.TAG_NAME,"button").click()
# delete_button=chrome.find_element(By.ID,"elements")
# assert delete_button.is_displayed()
# chrome.quit()
# #Test5
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
chrome.find_element(By.TAG_NAME,"button").click()
chrome.find_element(By.CLASS_NAME,"added-manually").click()
t = chrome.find_element(By.XPATH,"//*[@id='elements']/button")
assert t.is_displayed()
chrome.quit()
# #Test6
# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome.maximize_window()
# chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
# button=chrome.find_element(By.TAG_NAME,"button")
# for i in range(10):
#     button.click()
# #assert chrome.find_element(By.XPATH,"//*[@id='elements']/button[10]")
# lista_remove_buttons = chrome.find_element(By.ID,"elements")
# assert len(lista_remove_buttons) == 0
# chrome.quit()
# #Test7
# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome.maximize_window()
# chrome.get("https://cafeo.ro/")
# chrome.find_element(By.LINK_TEXT,"Contul meu").click()
# email_input = chrome.find_element(By.ID,"email")
# email_input.send_keys("abc@yahoo.com")
# chrome.find_element(By.ID,"passwd").send_keys("Alabala")
# chrome.find_element(By.CLASS_NAME,"submit").submit()
# assert chrome.find_element(By.CSS_SELECTOR,"[ class='alert alert-danger']")
#assert nu stiu
# chrome.quit()
# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome.maximize_window()
# chrome.get("https://www.tutorialspoint.com/about/about_careers.htm")
# chrome.find_element(By.PARTIAL_LINK_TEXT,"Refund")
# t = chrome.find_element(By.PARTIAL_LINK_TEXT,"Refund").is_displayed()
# if (t):
#     print('exista')
# sleep(4)