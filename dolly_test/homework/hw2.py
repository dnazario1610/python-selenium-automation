# ####PRACTICE WITH LOCATORS###
#
# #AMAZON LOGO
(By.XPATH, "//i[@class='a-icon a-icon-logo']")
# #
# # #email
(By.ID, 'ap_email')
# #
# # #continue
(By.ID, 'continue')
# #
# # #Conditions of use
(By.XPATH, "//a[text()='Conditions of Use']")
# #
#Privacy Notice
(By.XPATH, "//a[text()='Privacy Notice']")
# #
#Need Help
(By.XPATH, "//span[@class='a-expander-prompt']")
# #
# # #Forgot Password
(By.ID, 'auth-fpp-link-bottom')
# #
# # #Other issues with sign-in
(By.ID, 'ap-other-signin-issue-link')
# #
# # #Create Your Amazon account
(By.ID, 'createAccountSubmit')

#------------------------------------------------------------------------

##Test Case
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

driver.get('https://www.amazon.com')

driver.find_element(By.ID, 'nav-orders').click()

expected_result1 = 'Sign in'
actual_result1 = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert expected_result1 == actual_result1
print('Sign in header visible')

expected_result2 = 'Email or mobile phone number'
actual_result2 = driver.find_element(By.XPATH, "//label[@for='ap_email']").text
assert expected_result2 == actual_result2
print('Email input field present')

driver.quit()