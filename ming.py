#!/usr/bin/python

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import configparser
import sys, time
import datetime
import json
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import codecs


login_url = 'https://mijn.ing.nl/internetbankieren/SesamLoginServlet'

config = configparser.ConfigParser()
config.read('credential')
username = config.get('ing', 'username')
password = config.get('ing', 'password')
#driver = webdriver.PhantomJS()
#driver = webdriver.Chrome()
driver = webdriver.Chrome('/usr/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.set_window_size(1920, 1080)
driver.get(login_url)
user = driver.find_element_by_xpath("//input[@type='text']")
user.send_keys(username)
passwordlabel = driver.find_element_by_xpath('//*[@id="wachtwoord"]/label')
pasd = driver.find_element_by_xpath("//*[@id='{}']".format(passwordlabel.get_attribute("for")))
pasd.send_keys(password)
login_button = driver.find_element_by_xpath("//button[@class='submit']")
login_button.click()
time.sleep(2)

adv_button = driver.find_element_by_xpath('//*[@id="adv-search-txt"]')
adv_button.click()
cal_min = driver.find_element_by_xpath('//*[@id="dateRangeMin-input"]')
cal_max = driver.find_element_by_xpath('//*[@id="dateRangeMax-input"]')

cal_min.send_keys("01-03-2016")
cal_max.send_keys(datetime.datetime.now().strftime("%d-%m-%Y"))
time.sleep(3)
search_button = driver.find_element_by_xpath('//*[@id="form-submit-btnA"]')
search_button.click()
time.sleep(3)
more = driver.find_element_by_xpath('//*[@id="showMore"]')
while more.is_displayed():
    more.click()
    time.sleep(1.5)
time.sleep(3)
html_source = driver.page_source
fw = codecs.open("cc", 'w', encoding='utf8')
fw.write(html_source)
fw.close()
driver.close()
