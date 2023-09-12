from selenium import webdriver
from PIL import Image

# browser exposes an executable file

# Through Selenium test we will invoke the executable file which will then
# invoke actual browser
driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
# get method to launch the URL
driver.get("https://www.tutorialspoint.com/index.htm")
# to refresh the browser
driver.refresh()
# identifying the element to capture the screenshot
s = driver.find_element_by_xpath("//input[@class='gsc-input']")
# to get the element location
location = s.location
# to get the dimension the element
size = s.size
# to get the screenshot of complete page
driver.save_screenshot("screenshot_tutorialspoint.png")
# to get the x axis
x = location["x"]
# to get the y axis
y = location["y"]
# to get the length the element
height = location["y"] + size["height"]
# to get the width the element
width = location["x"] + size["width"]
# to open the captured image
imgOpen = Image.open("screenshot_tutorialspoint.png")
# to crop the captured image to size of that element
imgOpen = imgOpen.crop((int(x), int(y), int(width), int(height)))
# to save the cropped image
imgOpen.save("screenshot_tutorialspoint.png")
# to close the browser
driver.close()
