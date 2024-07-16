from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import csv

def write_field(xpath, field_data):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.send_keys(field_data)

def click_element(xpath):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()


REFERRAL_CODE = "GDSC-IN-7E6-E62"

line_no = 0
filename = "Gen_AI.csv"
with open(filename, "r") as file:
    reader = csv.reader(file)
    reader = list(reader)
    row = reader[line_no]
    mail_id = row[6]
    name = row[2]
    gender = row[3]
    graduation_year = row[4]
    profile_url = row[7]
    driver = webdriver.Chrome()


    # Navigate to the google form
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd70LmBmonFWIrh8MCAX_NjG0cXze07TCjEW-M-cXAXK9PU0w/formResponse")

    # Enter mail id
    write_field('/html/body/div/div[2]/form/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/input', mail_id)

    # Click next button
    click_element('/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')

    # Accept the terms
    click_element('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')

    # Click next button
    click_element('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')

    # Fill full name
    write_field('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input', name)

    # Select gender
    click_element('/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]')
    sleep(1)
    if gender == "Male":
        click_element('/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[4]/span')
    elif gender == "Female":
        click_element('/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]/span')
    sleep(1)

    # Select chapter
    click_element('/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]')
    sleep(1)
    click_element('/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[13]/span')
    sleep(1)

    # Enter referral code
    write_field('/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input', REFERRAL_CODE)

    # Select year of graduation
    click_element('/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    sleep(1)
    if graduation_year == "2024":
        click_element('/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div[3]/span')
    elif graduation_year == "2025":
        click_element('/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div[4]/span')
    elif graduation_year == "2026 or other":
        click_element('/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div[5]/span')
    sleep(1)

    # Laptop availability
    click_element('/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')

    # Click next button
    click_element('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')

    # Verifying if it is a new account
    click_element('/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div/label/div/div[1]/div/div[3]/div')

    # Enter mail id
    write_field('/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input', mail_id)

    # Click next button
    click_element('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')

    # Enter profile url
    write_field('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input', profile_url)

    # Acknowledge
    click_element('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div/label/div/div[1]/div/div[3]')
    click_element('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div/label/div/div[1]/div/div[3]')
    click_element('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div/label/div/div[1]/div/div[3]')


    # Submit
    click_element('/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[3]/div[1]/div[2]/span/span')
    sleep(50)
