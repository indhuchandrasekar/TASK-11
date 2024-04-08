from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def perform_drag_and_drop():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Open the URL
        driver.get("https://jqueryui.com/droppable")
        time.sleep(2)  # Wait for the page to load

        # Switch to the frame containing the draggable elements
        driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

        # Locate the draggable element
        draggable_element = driver.find_element(By.ID, "draggable")

        # Locate the droppable element
        droppable_element = driver.find_element(By.ID, "droppable")

        # Perform drag and drop action
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(draggable_element, droppable_element).perform()

        print("Drag and drop operation performed successfully.")

    finally:
        # Close the WebDriver
        driver.quit()

# Call the function to perform drag and drop operation
perform_drag_and_drop()

