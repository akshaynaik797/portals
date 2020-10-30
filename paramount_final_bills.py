import json
import os
from time import sleep
from urllib.parse import urlparse

from functions import driver, download_file
from functions import send_keys, click
from settings import WAIT_PERIOD

with open('temp.json') as json_file:
    data_dict = json.load(json_file)

website = data_dict['login_details']['website']
username = data_dict['login_details']['username']
password = data_dict['login_details']['password']

claimno, mss_no = data_dict['claim_no'], data_dict['mss_no']
# claimno = 4778769
doa, dod = data_dict['doa'], data_dict['dod']
wait_period = WAIT_PERIOD
amount = data_dict['amount']
remarks = data_dict['remark']
file_links = data_dict['docs']
files = []
for i, j in enumerate(file_links):
    file_name = os.path.basename(urlparse(j).path)
    download_file(j, f'attach/{mss_no}/{file_name}')
    files.append(os.path.abspath(f'attach/{mss_no}/{file_name}'))

username_input = '/html/body/form/div[3]/div[2]/div[1]/div/div/div/div[2]/fieldset/input[1]'
password_input = '/html/body/form/div[3]/div[2]/div[1]/div/div/div/div[2]/fieldset/input[2]'
login_btn = '/html/body/form/div[3]/div[2]/div[1]/div/div/div/div[2]/fieldset/input[3]'
e_cashless_btn = '/html/body/form/section/div/section/header/div[2]/li[2]'
enhancement_request_btn = '/html/body/form/section/div/section/header/div[2]/li[2]/ul/li[2]/a/span'
ccn_input = '/html/body/form/section/div/section/div/section/section/div/section/div/div[1]/div/div/input'
ccn_search_btn = '/html/body/form/section/div/section/div/section/section/div/section/div/div[2]/div/div/input'
request_for_option = '/html/body/form/section/div/section/div/section/section/div[2]/section/div/table/tbody/tr/td[1]/select/option[2]'
enhancement_request2_btn = '/html/body/form/section/div/section/div/section/section/div[2]/section/div/table/tbody/tr/td[2]/a'
# doa_input = '/html/body/form/section/div/ssplitextection/div/section/section/div[2]/section/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/input'
doa_input = '/html/body/form/section/div/section/div/section/section/div[2]/section/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/input'
dod_input = '/html/body/form/section/div/section/div/section/section/div[2]/section/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/input'
submit_btn = '/html/body/form/section/div/section/div/section/section/div[2]/section/div[2]/div[2]/div/div[3]/input[4]'
probalble_loss_btn = '/html/body/form/section/div/section/div/section/section/div[2]/section/div[2]/div[2]/div/div[2]/div/div[3]/div[1]/div/label'
total_amt_input = '/html/body/form/section/div/section/div/section/section/div[2]/section/div[1]/div[2]/div[2]/div/div/input'
remark_input = '/html/body/form/section/div/section/div/section/section/div[2]/section/div[1]/div[1]/div[2]/div/div/textarea'
drag_drop_input = '/html/body/form/section/div/section/div/section/section/div[2]/section/div[1]/div[3]/div/div[1]/div/input'
add_files_btn = '/html/body/form/section/div/section/div/section/section/div[2]/section/div[1]/div[3]/div/div[1]/div/div/input'

driver.get(website)
send_keys('xpath', username_input, username)
send_keys('xpath', password_input, password)
click('xpath', login_btn)
click('xpath', e_cashless_btn)
click('xpath', enhancement_request_btn)
send_keys('xpath', ccn_input, claimno)
click('xpath', ccn_search_btn)
click('xpath', request_for_option)
click('xpath', enhancement_request2_btn)
send_keys('xpath', doa_input, doa)
send_keys('xpath', dod_input, dod)
click('xpath', probalble_loss_btn)
click('xpath', submit_btn)
send_keys('xpath', total_amt_input, amount)
send_keys('xpath', remark_input, remarks)
for i in files:
    send_keys('xpath', drag_drop_input, os.path.abspath(i))
click('xpath', add_files_btn)
sleep(1000)
driver.close()
