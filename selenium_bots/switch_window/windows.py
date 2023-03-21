from selenium import webdriver
import time

def setUp():
    PATH = "C:\\Users\\User\\My Projects\\chromeDrivers\\chromedriver110\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=PATH)

    # URL = "write your url"
    driver.maximize_window()
    # driver.get(URL)
    return driver

driver = setUp()

# Opens a new tab
driver.execute_script("window.open()")
time.sleep(3)
# Switch to the newly opened tab
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

# Navigate to new URL in new tab
driver.get("https://google.com")
time.sleep(3)

# Switch to original tab
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

# Close original tab
driver.close()
time.sleep(3)

# Switch back to newly opened tab, which is now in position 0
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

# Close current tab
driver.close()
time.sleep(3)

# Switch back to original tab
driver.switch_to.window(driver.window_handles[0])