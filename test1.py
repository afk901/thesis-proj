from selenium import webdriver

chrome_binary_location = "./chrome/chrome.exe"
chromedriver_location = "./chromedriver/chromedriver.exe"
target_url = "https://google.com"

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_binary_location

# Create a Chrome driver with the specified options
driver = webdriver.Chrome()

# Navigate to the target URL
driver.get(target_url)

# Wait for the user to close the Chrome window
input("Press Enter to close the Chrome window...")

# Close the browser window
driver.quit()
