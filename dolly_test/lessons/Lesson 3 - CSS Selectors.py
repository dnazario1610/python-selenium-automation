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

# BY.ID
driver.find_element(By.ID, 'nav-search-submit-button')
driver.find_element(By.ID, ' nav-cart-count')

#CSS Selectors
#by Class(es) - Seperate with .
driver.find_element(By.CSS_SELECTOR, '.nav-input.nav-progressive-attribute')
driver.find_element(By.CSS_SELECTOR, '.nav-input')

#BY ID
driver.find_element(By.CSS_SELECTOR, '#nav-search-submit-button')

#By ID + Class
driver.find_element(By.CSS_SELECTOR, '#nav-search-submit-button.nav-input')

#BY ID + Class + Tag
driver.find_element(By.CSS_SELECTOR, 'input#nav-search-submit-button.nav-progressive-attribute.nave-input')

#BY Other attributes: [attribute='value']
driver.find_element(By.CSS_SELECTOR, "[name='field-keywords']")

#By class + other attributes: .class[attribute='value']
driver.find_element(By.CSS_SELECTOR, ".nav-input[type='text'][name='field-keywords']")

#BY Partial attribute
driver.find_element(By.CSS_SELECTOR, 'a[href*=ap_signin_notification_condition_of_use]')

#By parent - child element
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*='condition_of_use']")