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


login_page = 'https://mijn.ing.nl/internetbankieren/SesamLoginServlet'
redirect_page = 'https://bankieren.mijn.ing.nl/particulier/betalen/index'

click_id = 'advancedSearch'

datada_id = 'dateRangeMin-input'
dataa_id = 'dateRangeMax-input'
submit_id = 'form-submit-btnA'