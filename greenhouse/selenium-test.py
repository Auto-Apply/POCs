import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import os
dirname = os.path.dirname(__file__)


def clickSomething(driver, by, elementIdentifier):
    time.sleep(1)
    butt = driver.find_element(by, elementIdentifier).click()


def writeSomething(driver, by, elementIdentifier, text):
    time.sleep(1)
    butt = driver.find_element(by, elementIdentifier).send_keys(text)


def simplifyLogin(email, password):
    driver.switch_to.window(driver.window_handles[0])
    clickSomething(driver, By.XPATH, "//button[contains(., 'Got it!')]")
    clickSomething(driver, By.XPATH, "//a[contains(., 'Log in')]")
    writeSomething(driver, By.ID, "email", email)
    writeSomething(driver, By.ID, "password", password)
    clickSomething(driver, By.XPATH, "//button[contains(., 'Sign in')]")

    # Create a new instance of the browser driver
coptions = Options()
coptions.add_argument('--disable-gpu')
coptions.add_argument('--lang=en_US')
coptions.add_argument('disable-blink-features=AutomationControlled')
coptions.add_argument(
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36')
coptions.add_experimental_option('excludeSwitches', ['enable-logging'])
coptions.add_argument(
    '--load-extension={}'.format(os.path.join(dirname, 'extension_1_4_9_0')))
coptions.add_argument(
    '--user-data-dir={}'.format(os.path.join(dirname, 'state')))
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=coptions)


driver.delete_all_cookies()

# with open('cookies.pkl', 'rb') as f:
#     cookies = pickle.load(f)

# for cookie in cookies:
#     driver.add_cookie(cookie)

# simplifyLogin("skullcrusher2600@gmail.com", "Password123")

# time.sleep(1)
# print(driver.window_handles)
# driver.switch_to.window(driver.window_handles[1])

time.sleep(1)
driver.get("https://boards.greenhouse.io/tailscale/jobs/4038885005")

time.sleep(1)
job = driver.find_element(By.ID, "simplifyJobsContainer")
span = job.find_element(By.CSS_SELECTOR, ":first-child")
shadow_root = driver.execute_script("return arguments[0].shadowRoot", span)
got_it_button = shadow_root.find_element(By.ID, "fill-button")
print(got_it_button)
got_it_button.click()
print(shadow_root)
inner_html = span.get_attribute("innerHTML")

input()

# TODO
# Detect if signed in by reading text on widget button, perform next actions accordingly
