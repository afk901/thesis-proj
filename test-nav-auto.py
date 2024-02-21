from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# Function to list clickable links/buttons
def list_links(driver):
    return driver.find_elements(By.XPATH, "//a[@href] | //button")


# Main function to iterate through links and go back
def main():
    driver = webdriver.Firefox()  # Use Firefox browser
    driver.get(input("Enter the URL you want to visit: "))

    links = list_links(driver)
    num_links = len(links)
    if num_links == 0:
        print("No clickable links/buttons found.")
        driver.quit()
        return

    for i, link in enumerate(links, start=1):
        print(f"Visiting link {i}/{num_links}: {link.text}")
        link.click()
        driver.back()

    driver.quit()


# Run the main function
if __name__ == "__main__":
    main()
