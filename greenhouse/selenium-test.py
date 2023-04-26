import time
import ait 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager



# Create a new instance of the browser driver
coptions = Options()
coptions.add_argument('--disable-gpu')
coptions.add_argument('--lang=en_US')
coptions.add_argument('disable-blink-features=AutomationControlled')
coptions.add_argument('user-agent=fake-useragent')
coptions.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=coptions)
driver.delete_all_cookies()

# Navigate to a web page
time.sleep(2)
driver.get("https://boards.greenhouse.io/tailscale/jobs/4038885005")
time.sleep(1)
input_field = driver.find_element_by_id("first_name")
input_field.send_keys("Jason")
time.sleep(1)
input_field = driver.find_element_by_id("last_name")
input_field.send_keys("Brians")
time.sleep(1)
input_field = driver.find_element_by_id("email")
input_field.send_keys("jason12342@gmail.com")
time.sleep(1)
button = driver.find_element_by_xpath("//button[contains(@aria-describedby, 'resume-allowable-file-types')]")
button.click()

time.sleep(1)
ait.write(r'C:\Users\RemCa\OneDrive\Desktop\autoapply\jakes-resume.pdf')
time.sleep(1)
ait.press('enter')
time.sleep(1)

button = driver.find_element_by_id("submit_app")
button.click()
time.sleep(1)
# Find an element on the page and interact with it
time.sleep(100000)

# Close the browser