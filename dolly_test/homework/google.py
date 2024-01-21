from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.google.com')
driver.find_element(By.ID, 'APjFqb').send_keys('Pokemon')
driver.find_element(By.XPATH, "//input[@value='Google Search']").click()

expected_result = 'Pokemon'
actual_result = driver.find_element(By.XPATH, "//textarea[@type='search']").text
assert expected_result == actual_result
print('Test complete')

sleep(5)