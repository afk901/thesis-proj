from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_location = "./chrome/chrome.exe"
chromedriver_location = "./chromedriver/chromedriver.exe"

options = webdriver.ChromeOptions()
options.binary_location = chrome_location

chrome_service = Service(chromedriver_location)

# driver = webdriver.Chrome(service=chrome_service, options=options)
driver = webdriver.Firefox()

driver.maximize_window()


driver.get("https://www.python.org/")
# driver.get("https://www.free-css.com/assets/files/free-css-templates/preview/page295/sbs/")
# Scroll to the bottom of the page to load all content
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
time.sleep(2)  # Wait for content to load (you can adjust the sleep time)
# Get the total height of the page
total_height = driver.execute_script("return document.body.scrollHeight")
total_height += 500
# Set the window size to capture the entire page
driver.set_window_size(driver.get_window_rect()["width"], total_height)
# Capture the screenshot
driver.save_screenshot("screenshot.png")
driver.quit()
print("End...")
