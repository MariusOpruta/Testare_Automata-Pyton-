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
# assert chrome.find_element(By.TAG_NAME,"h4").is_displayed()
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
# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome.maximize_window()
# chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
# chrome.find_element(By.CSS_SELECTOR,"[onclick='addElement()']").click()
# chrome.find_element(By.CLASS_NAME,"added-manually").click()
# delete = chrome.find_elements(By.CLASS_NAME,"added-manually")
# assert len(delete)==0
# chrome.quit()
# Test6
# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome.maximize_window()
# chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
# button=chrome.find_element(By.TAG_NAME,"button")
# for i in range(10):
#     button.click()
# t = chrome.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')
# assert len(t)==10
# chrome.quit()
#Test7
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://cafeo.ro/")
chrome.find_element(By.CSS_SELECTOR,"[class='li_login last']").click()
chrome.find_element(By.ID,"SubmitLogin").submit()
email_input = chrome.find_element(By.ID,"email")
email_input.send_keys("aaasdfsdfd@yahoo.com")
chrome.find_element(By.ID,"passwd").send_keys("Assssla")
chrome.find_element(By.CLASS_NAME,"submit").submit()
sleep(4)
assert "Adresa de e-mail este invalida" in chrome.find_element(By.CSS_SELECTOR, "ol>li").text
#assert chrome.find_element(By.CSS_SELECTOR,"[class='alert alert-danger']") != "Am întâmpinat 1 problemă:"
#assert chrome.find_element(By.CSS_SELECTOR,"div[class='alert alert-danger']") == "Am întâmpinat 1 problemă:"
#assert chrome.find_element(By.CSS_SELECTOR,"div[class='alert alert-danger'] > p") == "Am întâmpinat 1 problemă:"
# assert chrome.find_element(By.CSS_SELECTOR,"[ol>li]") == "Adresa de email sau parola sunt greșite. Încearcă din nou."
#assert chrome.find_element(By.XPATH,"//*[@id='create-account_form']/div/p") == "Te rugăm să introduci adresa ta de email pentru a creea un cont nou."
chrome.quit()
