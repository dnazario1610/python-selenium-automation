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

###HOMEWORK Lesson 3###

#Amazon Logo
(By.CSS_Selector, '.a-icon.a-icon-logo')

#'Create Account'
(By.CSS_SELECTOR, '.a-spacing-small')

#Your Name
(By.CSS_SELECTOR, '#ap_customer_name')

#Email
(By.CSS_SELECTOR, '#ap_email')

#Password
(By.CSS_SELECTOR, '#ap_password')

#Re-Enter Password
(By.CSS_SELECTOR, '#ap_password_check')

#Create your account button
(By.CSS_SELECTOR, '#continue')

#Conditions
(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use?']")

#Privary Notice
(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")

#SignIN
(By.CSS_SELECTOR, '.a-link-emphasis')