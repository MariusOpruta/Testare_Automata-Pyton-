from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Test1
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/login")
text_welcome = chrome.find_element(By.TAG_NAME, "h2")
assert text_welcome.text=="Login Page"
#assert len(text_welcome)==10
#Test2
chrome.find_element(By.LINK_TEXT,"Elemental Selenium").click()
driver = webdriver.Chrome()
driver.execute_script("window.open('','_blank');")
def test_url(self):
    actual = self.chrome.current_url
    expected = 'https://the-internet.herokuapp.com/login'
    self.assertEqual(expected, actual, 'URL-ul nu este corect')
chrome.quit()
#Test3
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/login")
username_input = chrome.find_element(By.ID,"username")
username_input.send_keys("tomsmith")
chrome.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
chrome.find_element(By.CLASS_NAME,"radius").click()
chrome.find_element(By.CSS_SELECTOR, "[href='/logout']").click()
assert text_welcome.text=="Login Page"
chrome.quit()
#Test4
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
chrome.find_element(By.CLASS_NAME,"example").send_keys()

sleep(10)

