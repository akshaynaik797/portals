import base64
import os
from time import sleep

from settings import driver, EC, WebDriverWait, By

website = 'https://provider.ihx.in/#/'
username, password = 'amitmehta1000976@medibuddy.in', 'ppg@1234'
claimno = '101600276'

file_name = 'capcha.jpeg'
wait_period = 20


captcha_xpath = '/html/body/div[1]/section/section/div[3]/form/div[3]/div[2]/img'
captcha_enter_xpath = '/html/body/div[1]/section/section/div[3]/form/div[3]/div[1]/input'
username_xpath = '/html/body/div[1]/section/section/div[3]/form/div[1]/input'
password_xpath = '//*[@id="exampleInputPassword1"]'
sign_in_xpath = '/html/body/div[1]/section/section/div[3]/form/div[4]/div/button[1]'
cancel_bt_xpath = '/html/body/div[1]/div/div/form/div[2]/button'

claim_no_option_xpath = '/html/body/div[1]/section/header/div[1]/div[1]/div/div[1]/div/select/option[2]'
claim_no_field_xpath = '//*[@id="claimSearchFormClaimNo"]'
claim_no_name = 'claimNo'
claim_no_search_button_xpath = '/html/body/div[1]/section/header/div[1]/div[1]/div/div[2]/form[1]/div[2]/div[2]/span/button[1]/i'

row_xpath = '/html/body/div[1]/section/section/div/div[1]/div[1]/angular-tab/div[1]/div[1]/div/div/div[1]/div[5]'

driver.get(website)
WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, username_xpath))).send_keys(username)
WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, password_xpath))).send_keys(password)

src = WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, captcha_xpath))).get_attribute("src")
with open(file_name, "wb") as fp:
    temp = src.partition(',')[2]
    fp.write(base64.decodebytes(bytes(temp, encoding='utf8')))
captcha_input = input('Enter capcha data:')
if os.path.exists(file_name):
    os.remove(file_name)
WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, captcha_enter_xpath))).send_keys(captcha_input)
WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, sign_in_xpath))).click()
sleep(4)
if driver.current_url == 'https://provider.ihx.in/#/claims/':
    WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, cancel_bt_xpath))).click()
    WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, claim_no_option_xpath))).click()
    WebDriverWait(driver, wait_period).until(
        EC.visibility_of_element_located((By.NAME, claim_no_name))).send_keys(claimno)
    WebDriverWait(driver, wait_period).until(
        EC.visibility_of_element_located((By.XPATH, claim_no_search_button_xpath))).click()
driver.close()
