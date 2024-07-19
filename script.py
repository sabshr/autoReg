from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta

# Set the URL of the registration page
url = 'https://sis.jhu.edu/sswf/SSS/EnrollmentCart/SSS_EnrollmentCart.aspx?MyIndex=171958'  # Replace with the actual URL

# Set the predetermined date and time to start clicking (July 22nd at 4:00 AM PST -- 7:00 EST)
target_time = datetime(2024, 7, 22, 4, 0, 0)  # Adjust the year, month, day, hour, minute, second as needed

# Path to the WebDriver (make sure to adjust the path according to your setup)
driver_path = '/path/to/your/webdriver'  # Replace with your WebDriver path

# Initialize the WebDriver (using Chrome in this example)
driver = webdriver.Chrome(driver_path)

# Open the registration page
driver.get(url)

# Calculate the time difference between now and the target time
current_time = datetime.now()
time_difference = (target_time - current_time).total_seconds()

# Wait until the predetermined date and time
if time_difference > 0:
    time.sleep(time_difference)

# Find and click the "Add to Cart" button
add_to_cart_button = driver.find_element(By.ID, 'ct100_contentPlaceHolder1_btnAddToCart')
add_to_cart_button.click()

# Wait a short time to ensure the first action is completed
time.sleep(2)

# Find and click the checkbox to select all classes
select_all_checkbox = driver.find_element(By.ID, 'SelectAllCheckBox')
select_all_checkbox.click()

# Find and click the "Register" button
register_button = driver.find_element(By.XPATH, '//button[contains(text(), "Register")]')
register_button.click()

# Close the browser after clicking
time.sleep(5)  # Adjust the sleep time if needed to ensure registration completes
driver.quit()