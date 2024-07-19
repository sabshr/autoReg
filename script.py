#!/usr/bin/env python3

#INSTRUCTIONS:
# Run this command in bash or zsh before running!
#/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/Users/sabshr/Library/Application Support/Google/Chrome/Default"
# Run program once. If needed, log into SIS so a session is active.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

# Set the URL of the registration page
url = 'https://sis.jhu.edu/sswf/SSS/EnrollmentCart/SSS_EnrollmentCart.aspx?MyIndex=171958'  # Replace with the actual URL

# Set the predetermined date and time to start clicking (July 22nd at 4:00 AM PST / 7:00 AM EST)
target_time = datetime(2024, 7, 19, 1, 53, 0)  # year, month, day, hour, minute, second

# Remote debugging port
debugging_address = "localhost:9222"

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", debugging_address)

try:
    driver = webdriver.Chrome(options=options)
    print("Connected to existing Chrome session.")

    # Open a new tab
    driver.execute_script("window.open('');")
    time.sleep(1)

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])

    # Open the registration page in the new tab
    driver.get(url)
    print("Tab Opened.")

    # Calculate the time difference between now and the target time
    current_time = datetime.now()
    time_difference = (target_time - current_time).total_seconds()

    # Wait until the predetermined date and time
    if time_difference > 0:
        print(f"Waiting for {time_difference} seconds until the target time.")
        time.sleep(time_difference)

    # Finds and clicks the checkbox after delay to select all classes (doesn't work w'o delay for some weird reason??)
    checkbox = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.ID, "SelectAllCheckBox"))
    )
    checkbox.click()
    print("Clicked 'Select All' checkbox.")

    # Find and click the "Register" button
    register_button = driver.find_element(By.ID, "ctl00_contentPlaceHolder_ibEnroll")
    register_button.click()
    print("Clicked 'Register' button.")

    # Close the browser after clicking
    time.sleep(1)  # Adjust the sleep time if needed to ensure registration completes
    driver.quit()
    print("Browser closed.")

except Exception as e:
    print(f"An error occurred: {e}")
    if driver:
        driver.quit()