from selenium import webdriver
import time

PATH = "C:\\Users\\User\\My Projects\\chromeDrivers\\chromedriver110\\chromedriver.exe"
URL = "https://google.com"

print("INFO: Running Chrome Driver")
driver = webdriver.Chrome(executable_path=PATH)
print("INFO: Opening URL")
driver.get(URL)
time.sleep(2)
print("INFO: Closing Chrome Driver")
driver.close()
driver.quit()