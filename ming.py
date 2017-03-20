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


login_url = 'https://mijn.ing.nl/internetbankieren/SesamLoginServlet'
redirect_page = 'https://bankieren.mijn.ing.nl/particulier/betalen/index'

click_id = 'advancedSearch'

datada_id = 'dateRangeMin-input'
dataa_id = 'dateRangeMax-input'
submit_id = 'form-submit-btnA'
more_id = 'showMore'


config = configparser.ConfigParser()
config.read('credential')
username = config.get('ing', 'username')
password = config.get('ing', 'password')
#driver = webdriver.PhantomJS()
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get(login_url)
user = driver.find_element_by_xpath("//input[@type='text']")
pasd = driver.find_element_by_xpath("//input[@type='password']")
user.send_keys(username)
pasd.send_keys(password)
login_button = driver.find_element_by_xpath("//button[@class='submit']")
login_button.click()
time.sleep(2)
