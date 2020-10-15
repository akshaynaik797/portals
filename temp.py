import base64
import os
from time import sleep

# from settings import driver, EC, WebDriverWait, By
from functions import click, send_keys, get_attribute, driver, drag_and_drop_file

website = 'https://provider.ihx.in/#/'
username, password = 'amitmehta1000976@medibuddy.in', 'ppg@1234'
claimno = '101600276'
doa, dod = '10/14/2020', '10/14/2020'
xpath = 'xpath'
file_name = 'capcha.jpeg'
wait_period = 25


captcha_img_xpath = '/html/body/div[1]/section/section/div[3]/form/div[3]/div[2]/img'
captcha_enter_xpath = '/html/body/div[1]/section/section/div[3]/form/div[3]/div[1]/input'
username_xpath = '/html/body/div[1]/section/section/div[3]/form/div[1]/input'
password_xpath = '//*[@id="exampleInputPassword1"]'
sign_in_xpath = '/html/body/div[1]/section/section/div[3]/form/div[4]/div/button[1]'
cancel_bt_xpath = '/html/body/div[1]/div/div/form/div[2]/button'

claim_no_option_xpath = '/html/body/div[1]/section/header/div[1]/div[1]/div/div[1]/div/select/option[2]'
claim_no_name = 'claimNo'
claim_no_search_button_xpath = '/html/body/div[1]/section/header/div[1]/div[1]/div/div[2]/form[1]/div[2]/div[2]/span/button[1]/i'

status_btn_xpath = '/html/body/div[1]/section/section/div/div[1]/div[1]/angular-tab/div[1]/div[1]/div/div/div[1]/div[5]/table/tbody/tr/td[6]/span[6]'
upload_files_xpath = '/html/body/div[1]/section/section/div/div[1]/div[1]/angular-tab/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div/hosp-action/div[1]/button'
doa_input_xpath = '/html/body/div[1]/div/div/div[2]/form/div/div[1]/div/input'
dod_input_xpath = '/html/body/div[1]/div/div/div[2]/form/div/div[2]/div/input'
dates_submit_btn_xpath = '/html/body/div[1]/div/div/div[3]/button'
files_upload_btn_xpath = '/html/body/div[1]/div/div/div/form/div[1]/div[4]/div/div[2]/div[1]/div'
amount_input_xpath = '/html/body/div[1]/div/div/div/form/div[1]/div[2]/div[4]/div/input'
remarks_input_xpath = '/html/body/div[1]/div/div/div/form/div[1]/div[3]/textarea'
temp_xpath = '//*[@id="holder"]'
website = "https://bestvpn.org/html5demos/file-api/"
driver.get(website)
a = driver.find_element_by_xpath(temp_xpath)
drag_and_drop_file(a, os.path.abspath('capcha.jpeg'))



driver.get(website)
send_keys(xpath,username_xpath,username)
send_keys(xpath,password_xpath,password)
src = get_attribute(xpath, captcha_img_xpath, 'src')
with open(file_name, "wb") as fp:
    temp = src.partition(',')[2]
    fp.write(base64.decodebytes(bytes(temp, encoding='utf8')))
captcha_input = input('Enter capcha data:')
send_keys(xpath, captcha_img_xpath, captcha_input)
click(xpath, sign_in_xpath)

WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, captcha_enter_xpath))).send_keys(captcha_input)
WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, sign_in_xpath))).click()


WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, username_xpath))).send_keys(username)
WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, password_xpath))).send_keys(password)
src = WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, captcha_img_xpath))).get_attribute("src")
with open(file_name, "wb") as fp:
    temp = src.partition(',')[2]
    fp.write(base64.decodebytes(bytes(temp, encoding='utf8')))
captcha_input = input('Enter capcha data:')
if os.path.exists(file_name):
    os.remove(file_name)
WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, captcha_enter_xpath))).send_keys(captcha_input)
WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, sign_in_xpath))).click()


WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, cancel_bt_xpath))).click()
WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, claim_no_option_xpath))).click()
WebDriverWait(driver, wait_period).until(
    EC.visibility_of_element_located((By.NAME, claim_no_name))).send_keys(claimno)
WebDriverWait(driver, wait_period).until(
    EC.visibility_of_element_located((By.XPATH, claim_no_search_button_xpath))).click()
WebDriverWait(driver, wait_period).until(
    EC.visibility_of_element_located((By.XPATH, status_btn_xpath))).click()
WebDriverWait(driver, wait_period).until(
    EC.visibility_of_element_located((By.XPATH, upload_files_xpath))).click()
WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, doa_input_xpath))).send_keys(
    doa)
WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, dod_input_xpath))).send_keys(
    dod)
WebDriverWait(driver, wait_period).until(
    EC.visibility_of_element_located((By.XPATH, dates_submit_btn_xpath))).click()
WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, amount_input_xpath))).send_keys(
    '999')
WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, remarks_input_xpath))).send_keys(
    'discharge')
# WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, files_upload_btn_xpath))).click()
# WebDriverWait(driver, wait_period).until(EC.element_to_be_clickable((By.XPATH, files_upload_btn_xpath))).click()
sleep(60)
driver.close()

