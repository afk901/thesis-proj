from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to list clickable links/buttons and ask for user input
def list_and_choose_links(driver):
    links = driver.find_elements(By.XPATH, "//a[@href] | //button")
    print("Clickable Links/Buttons:")
    for i, link in enumerate(links, start=1):
        print(f"{i}. {link.text}")
    choice = input("Enter the number corresponding to the link/button you want to click (or 'q' to quit): ")
    if choice.lower() == 'q':
        return None
    try:
        choice_index = int(choice) - 1
        if choice_index >= 0 and choice_index < len(links):
            return links[choice_index]
        else:
            print("Invalid choice! Please enter a valid number.")
            return list_and_choose_links(driver)
    except ValueError:
        print("Invalid choice! Please enter a valid number.")
        return list_and_choose_links(driver)

# Main function to perform the tasks repeatedly until user opts to quit
def main():
    driver = webdriver.Firefox()  # Use Firefox browser
    while True:
        driver.get(input("Enter the URL you want to visit: "))
        while True:
            clickable_element = list_and_choose_links(driver)
            if clickable_element is None:
                break
            clickable_element.click()
            WebDriverWait(driver, 10).until(EC.staleness_of(clickable_element))
        if input("Do you want to continue browsing? (y/n): ").lower() != 'y':
            break
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
