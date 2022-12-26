from selenium import webdriver
driver=webdriver.Chrome(executable_path="D:\\dammy\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
print(driver.current_url)
driver.find_element_by_id("name").send_keys("manish")
driver.find_element_by_xpath("//input[@id='alertbtn']").click()