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

#BY XPATH
driver.find_element(By.XPATH, "//a[data-csa-c-content-id='nav_cs_bestsellers']")
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")

#MULTIPLE ATTRIBUTES
driver.find_element(By.XPATH, "//a[@class='nav-a  ' and @data-csa-c-content-id='nav_cs_bestsellers']")

#BY XPATH, TEXT
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

#CONTAINS
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers']")
driver.find_element(By.XPATH, "//a[contains(text(), 't Seller') and @class='nav-a  ']")


