#!/usr/bin/env python3

#INSTRUCTIONS:
# Run this command in bash or zsh before running!
#/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/Users/sabshr/Library/Application Support/Google/Chrome/Default"
# Run program once. If needed, log into SIS so a session is active.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

# Set the URL of the registration page
url = 'https://sis.jhu.edu/sswf/SSS/EnrollmentCart/SSS_EnrollmentCart.aspx?MyIndex=171958'  # Replace with the actual URL

# Set the predetermined date and time to start clicking (July 22nd at 4:00 AM PST / 7:00 AM EST)
target = datetime(2024, 7, 19, 1, 53, 0)  # year, month, day, hour, minute, second

# Remote debugging port
debugging_address = "localhost:9222"
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", debugging_address)

try:
    with webdriver.Chrome(options=options) as driver:
        print("Connected to existing Chrome session.")

        # Open a new tab and switch to it
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])

        # Open the registration page in the new tab
        driver.get(url)
        print("Tab Opened.")

        # Wait until the predetermined date and time
        timeDelta = (target - datetime.now()).total_seconds()
        if timeDelta > 0:
            print(f"Waiting for {timeDelta:.2f} seconds until the target time.")
            WebDriverWait(driver, timeDelta).until(
                EC.presence_of_element_located((By.ID, "SelectAllCheckBox"))
            )

        # Finds and clicks the checkbox to select all classes
        checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "SelectAllCheckBox"))
        )
        checkbox.click()
        print("Clicked 'Select All' checkbox.")

        # Find and click the "Register" button
        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ctl00_contentPlaceHolder_ibEnroll"))
        )
        register_button.click()
        print("Clicked 'Register' button.")

        # Wait to ensure the registration completes
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element((By.ID, "ctl00_contentPlaceHolder_ibEnroll"))
        )
        print("Completed.")

except Exception as e:
    print(f"An error occurred: {e}")