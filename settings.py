from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


webdriver_path = '/home/akshay/Downloads/chromedriver'
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(webdriver_path, options=chrome_options)
