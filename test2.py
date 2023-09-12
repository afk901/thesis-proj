from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

chrome_binary_location = "./chrome/chrome.exe"
chromedriver_location = "./chromedriver/chromedriver.exe"
log_file = "website_log.txt"

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_binary_location

# Create a Chrome service
chrome_service = Service(chromedriver_location)

# Create a Chrome driver with the specified service and options
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


# Function to log website access
def log_website_access(url, title):
    current_time = time.strftime("%H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"{current_time} - URL: {url}, Title: {title}\n")


# Start an infinite loop to track website changes
try:
    previous_url = None
    while True:
        current_url = driver.current_url
        current_title = driver.title
        time.sleep(2)  # Check every 2 seconds

        # If the URL changes, log the access
        if current_url != previous_url:
            log_website_access(current_url, current_title)
            previous_url = current_url
except KeyboardInterrupt:
    pass

# Close the browser window
driver.quit()
