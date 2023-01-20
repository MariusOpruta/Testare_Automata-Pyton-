from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


#Test1
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/login")
text_welcome = chrome.find_element(By.TAG_NAME, "h2")
assert text_welcome.text=="Login Page"
chrome.find_element(By.TAG_NAME,"h4")=="This is where you can log into the secure area. Enter  for the username and  for the password. If the information is wrong you should see error messages."
chrome.quit()
#Test2
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/login")
chrome.find_element(By.LINK_TEXT,"Elemental Selenium").click()
driver = webdriver.Chrome()
driver.execute_script("window.open('','_blank');")
def test_url(self):
    actual = self.chrome.current_url
    expected = 'https://the-internet.herokuapp.com/login '
    self.assertEqual(expected, actual, 'URL-ul nu este corect')
chrome.quit()
# #Test3
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/login")
username_input = chrome.find_element(By.ID,"username")
username_input.send_keys("tomsmith")
chrome.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
chrome.find_element(By.CLASS_NAME,"radius").click()
chrome.find_element(By.CSS_SELECTOR, "[href='/logout']").click()
assert chrome.current_url=="https://the-internet.herokuapp.com/login"
chrome.quit()
# #Test4
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
chrome.find_element(By.TAG_NAME,"button").click()
delete_button=chrome.find_element(By.ID,"elements")
assert delete_button.is_displayed()
chrome.quit()
# # Test5
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
chrome.find_element(By.TAG_NAME,"button").click()
chrome.find_element(By.CLASS_NAME,"added-manually").click()
# t=chrome.find_element(By.CLASS_NAME,"added-manually").size()
# if (t==0):
#     print('Butonul nu exista')
# else:
#     print('Butonul exista')

# chrome.quit()
# Test6
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
button=chrome.find_element(By.TAG_NAME,"button")
for i in range(10):
    button.click()
t = chrome.find_element(By.ID,"elements").size(10)
assert t==10

chrome.quit()
#Test7
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://cafeo.ro/")
chrome.find_element(By.LINK_TEXT,"Contul meu").click()
email_input = chrome.find_element(By.ID,"email")
email_input.send_keys("abc@yahoo.com")
chrome.find_element(By.ID,"passwd").send_keys("Alabala")
#chrome.find_element(By.CLASS_NAME, "button btn btn-default button-medium button-2action").click()
#chrome.find_element(By.ID,"SubmitLogin").click()
#assert chrome.find_element(By.CLASS_NAME,"alert alert-danger"),"Am întâmpinat 1 problemă:"
sleep(10)

