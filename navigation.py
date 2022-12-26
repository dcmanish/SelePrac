from selenium import webdriver
driver=webdriver.Chrome(executable_path="D:\\dammy\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)