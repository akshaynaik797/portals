import base64
import json
import os
from time import sleep

from functions import download_file
from functions import drag_and_drop_file, send_keys, click, get_attribute
from functions import driver, EC, WebDriverWait, By
from gui_functions import capcha_popup
from settings import WAIT_PERIOD
from make_log import log_exceptions

try:
    with open('temp.json') as json_file:
        data_dict = json.load(json_file)


    website = data_dict['login_details']['website']
    username = data_dict['login_details']['username']
    password = data_dict['login_details']['password']

    claimno = data_dict['claim_no']
    doa, dod = data_dict['doa'], data_dict['dod']
    file_name = 'capcha.jpeg'
    wait_period = int(WAIT_PERIOD)
    amount = data_dict['amount']
    remarks = data_dict['remark']
    file_links = data_dict['docs']
    files = []
    for i, j in enumerate(file_links):
        download_file(j, f'attach/{i}.pdf')
        files.append(os.path.abspath(f'attach/{i}.pdf'))

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
    # drag_drop_xpath = '/html/body/div[1]/div/div/div/div[1]/ng-form/div[3]/div/div[1]'
    drag_drop_xpath = '/html/body/div[1]/div/div/div/form/div[1]/div[4]/div/div[2]/div[1]/div'


    driver.get(website)
    # click('xpath', cancel_bt_xpath)
    send_keys('xpath', username_xpath, username)
    send_keys('xpath', password_xpath, password)
    src = get_attribute('xpath', captcha_img_xpath, "src")
    with open(file_name, "wb") as fp:
        temp = src.partition(',')[2]
        fp.write(base64.decodebytes(bytes(temp, encoding='utf8')))
    captcha_input = capcha_popup()
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
except:
    log_exceptions()