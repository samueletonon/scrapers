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


fr = open("cc",'r')
html_source = fr.read()
fr.close()
soup = BeautifulSoup(html_source)
table = soup.findAll(id="receivedTransactions")[0]
tbody = table.findAll("tbody")[1]
for tr in tbody.findAll("tr")
 ##
