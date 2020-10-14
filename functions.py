from time import sleep
from requests import get  # to make GET request
from settings import driver, EC, WebDriverWait, By, TimeoutException
from make_log import log_exceptions

wait_period = 10


def download_file(url, file_name):
    # open in binary mode
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
                try:
                    WebDriverWait(driver, wait). \
                        until(EC.visibility_of_element_located((By.XPATH, path_value))).click()
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
                    driver.find_element_by_xpath(path_value).send_keys('asd')
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
