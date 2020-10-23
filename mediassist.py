import base64
import os
from time import sleep
from tkinter import messagebox
from functions import drag_and_drop_file, send_keys, click, get_attribute
from functions import driver, EC, WebDriverWait, By

website = 'https://provider.ihx.in/#/'
username, password = 'amitmehta1000976@medibuddy.in', 'ppg@1234'

claimno = '23030097'
doa, dod = '10/23/2020', '10/23/2020'
file_name = 'capcha.jpeg'
wait_period = 25
amount = '999'
remarks = 'discharge'
files = ['img.jpg']


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
drag_drop_xpath = '/html/body/div[1]/div/div/div/form/div[1]/div[4]/div/div[2]/div[1]/div'


driver.get(website)
send_keys('xpath', username_xpath, username)
send_keys('xpath', password_xpath, password)
src = get_attribute('xpath', captcha_img_xpath, "src")
with open(file_name, "wb") as fp:
    temp = src.partition(',')[2]
    fp.write(base64.decodebytes(bytes(temp, encoding='utf8')))
captcha_input = input('Enter capcha data:')
if os.path.exists(file_name):
    os.remove(file_name)
send_keys('xpath', captcha_enter_xpath, captcha_input)
click('xpath', sign_in_xpath)
click('xpath', cancel_bt_xpath)
click('xpath', claim_no_option_xpath)
send_keys('name', claim_no_name, claimno)
click('xpath', claim_no_search_button_xpath)
click('xpath', status_btn_xpath)
click('xpath', upload_files_xpath)
send_keys('xpath', doa_input_xpath, doa)
send_keys('xpath', dod_input_xpath, dod)
click('xpath', dates_submit_btn_xpath)
send_keys('xpath', amount_input_xpath, amount)
send_keys('xpath', remarks_input_xpath, remarks)
a = WebDriverWait(driver, wait_period).until(EC.visibility_of_element_located((By.XPATH, drag_drop_xpath)))
for i in files:
    drag_and_drop_file(a, os.path.abspath(i))
sleep(60)
driver.close()
