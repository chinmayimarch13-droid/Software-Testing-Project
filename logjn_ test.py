from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://example.com/login")

driver.find_element(By.ID,"username").send_keys("testuser")
driver.find_element(By.ID,"password").send_keys("12345")

driver.find_element(By.ID,"login").click()

print("Login Test Executed")

driver.quit()
