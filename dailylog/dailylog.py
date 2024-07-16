from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def click_element(xpath):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

def write_field(xpath, field_data):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.send_keys(field_data)


mail_id = "arvindh.it23@bitsathy.ac.in"
password = "Arvindh@1211"
name = "ARVINDH S"
register_number = "7376232IT114"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Initiate WebDriver and manage its version
driver = webdriver.Chrome(options=options)

# Navigate to Daily Log Form
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe0ufG6EwtPxgb_c4IJ340fwCzFOdIJ7U7z9b8Bws6SXVaaWw/viewform?vc=0&c=0&w=1&flr=0&pli=1")

# Enter email address
email_field =WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierId"]')))
email_field.send_keys(mail_id)
email_field.send_keys(Keys.ENTER)

# Enter password
password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)

# Click the check box
click_element('//*[@id="i5"]')

# Enter register number
write_field('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
            register_number)

# Choose an option in Today's Engagement Field (Self Learning)
click_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
click_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[7]')

# Click Next button
click_element('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

# Fill FN Session details
write_field('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea',
            'Chemistry')

# Fill AN Session details
write_field('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea',
            'Maths')

# Click Next button
click_element('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')

# Enter FA score
write_field('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
            'No FA')

time.sleep(10)
