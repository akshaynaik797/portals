from time import sleep
import os

from requests import get
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from gui_functions import wait_popup
from make_log import log_exceptions
from settings import WAIT_PERIOD, WEBDRIVER_FOLDER_PATH

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(WEBDRIVER_FOLDER_PATH, options=chrome_options)
wait_period = int(WAIT_PERIOD)


def download_file(url, file_name):
    # open in binary mode
    if not os.path.exists(os.path.split(file_name)[0]):
        os.mkdir(os.path.split(file_name)[0])
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)


def click(by, path_value):
    global wait_period
    wait = wait_period
    if by == 'xpath':
        try:
            WebDriverWait(driver, wait) \
                .until(EC.visibility_of_element_located((By.XPATH, path_value))).click()
            return True
        except TimeoutException:
            while 1:
                state = wait_popup()
                try:
                    if state == True:
                        WebDriverWait(driver, wait) \
                            .until(EC.visibility_of_element_located((By.XPATH, path_value))).click()
                        return 1
                    else:
                        return 0
                except TimeoutException:
                    continue
        except:
            log_exceptions()
            return False
    else:
        return False


def send_keys(by, path_value, input):
    global wait_period
    wait = wait_period
    if by == 'xpath':
        try:
            WebDriverWait(driver, wait) \
                .until(EC.visibility_of_element_located((By.XPATH, path_value))).send_keys(input)
            return True
        except TimeoutException:
            while 1:
                try:
                    WebDriverWait(driver, wait). \
                        until(EC.visibility_of_element_located((By.XPATH, path_value))).send_keys(input)
                    return True
                except TimeoutException:
                    wait = wait * 2
                    print(f"waiting for {wait} seconds.")
                    sleep(wait)
                    continue
                except:
                    log_exceptions()
                    return False
        except:
            log_exceptions()
            return False
    elif by == 'name':
        try:
            WebDriverWait(driver, wait) \
                .until(EC.visibility_of_element_located((By.NAME, path_value))).send_keys(input)
            return True
        except TimeoutException:
            while 1:
                try:
                    WebDriverWait(driver, wait). \
                        until(EC.visibility_of_element_located((By.NAME, path_value))).send_keys(input)
                    return True
                except TimeoutException:
                    wait = wait * 2
                    print(f"waiting for {wait} seconds.")
                    sleep(wait)
                    continue
                except:
                    log_exceptions()
                    return False
        except:
            log_exceptions()
            return False
    else:
        return False


def get_attribute(by, path_value, attribute):
    global wait_period
    wait = wait_period
    if by == 'xpath':
        try:
            value = WebDriverWait(driver, wait) \
                .until(EC.visibility_of_element_located((By.XPATH, path_value))).get_attribute(attribute)
            return value
        except TimeoutException:
            while 1:
                try:
                    value = WebDriverWait(driver, wait) \
                        .until(EC.visibility_of_element_located((By.XPATH, path_value))).get_attribute(attribute)
                    return value
                except TimeoutException:
                    wait = wait * 2
                    print(f"waiting for {wait} seconds.")
                    sleep(wait)
                    continue
                except:
                    log_exceptions()
                    return False
        except:
            log_exceptions()
            return False
    else:
        return False


JS_DROP_FILE = """
    var target = arguments[0],
        offsetX = arguments[1],
        offsetY = arguments[2],
        document = target.ownerDocument || document,
        window = document.defaultView || window;

    var input = document.createElement('INPUT');
    input.type = 'file';
    input.onchange = function () {
      var rect = target.getBoundingClientRect(),
          x = rect.left + (offsetX || (rect.width >> 1)),
          y = rect.top + (offsetY || (rect.height >> 1)),
          dataTransfer = { files: this.files };

      ['dragenter', 'dragover', 'drop'].forEach(function (name) {
        var evt = document.createEvent('MouseEvent');
        evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
        evt.dataTransfer = dataTransfer;
        target.dispatchEvent(evt);
      });

      setTimeout(function () { document.body.removeChild(input); }, 25);
    };
    document.body.appendChild(input);
    return input;
"""


def drag_and_drop_file(drop_target, path):
    driver = drop_target.parent
    file_input = driver.execute_script(JS_DROP_FILE, drop_target, 0, 0)
    file_input.send_keys(path)
    pass