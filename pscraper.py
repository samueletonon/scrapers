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

login_url = 'https://account.lycamobile.nl/login.aspx?lang=en'
credithistory_url = 'https://account.lycamobile.nl/TopUp/CdrReport.aspx?lang=en'

def lycamobile():
    config = configparser.ConfigParser()
    config.read('credential')
    username = config.get('lyca', 'username')
    password = config.get('lyca', 'password')
    driver = webdriver.PhantomJS()
    #driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.get(login_url)
    user = driver.find_element_by_id('ctl00_cphPro_txtMobileNumber')
    pasd = driver.find_element_by_id('ctl00_cphPro_txtPassword')
    user.send_keys(username)
    pasd.send_keys(password)
    login_button = driver.find_element_by_id('ctl00_cphPro_btnLogin')
    login_button.click()
    time.sleep(2)
    xx = driver.find_element_by_xpath('//div[@class="nub-bal-date-detail"]/span')
    if xx.text != username:
        #login failed
        sys.exit(2)

    listone = []
    driver.get(credithistory_url)
    select = driver.find_element_by_id('ctl00_cphPro_ddlListPeriod')
    optionl = select.find_elements_by_tag_name('option')
    count = 0
    while count < len(optionl):
        if count != 0:
            driver.get(credithistory_url)
            select = driver.find_element_by_id('ctl00_cphPro_ddlListPeriod')
            optionl = select.find_elements_by_tag_name('option')
            option = optionl[count]
            option.click()
            time.sleep(10)
            sbm = driver.find_element_by_id('ctl00_cphPro_btnSubmit')
            sbm.click()
        count = count + 1
        EndMonth = 0
        while EndMonth == 0:
            # BS4 routine
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            element_present = EC.presence_of_element_located((By.ID, 'ctl00_cphPro_trAdobe'))
            WebDriverWait(driver, 10).until(element_present)
            soup = BeautifulSoup(driver.page_source)
            table = soup.find(id='ctl00_cphPro_grdBillDetails')
            for tr in table.findAll('tr', { "class" : "tbl-data" }):
                tdlist = tr.findAll('td')
                obj = {}
                obj['type'] = tdlist[0].text
                seconds = tdlist[3].text.split(':')
                if len(seconds) == 3:
                    obj['duration'] = int(seconds[0]) * 3600 + int(seconds[1]) * 60 + int(seconds[2])
                else:
                    print seconds
                obj['cost'] = float(tdlist[4].text)
                #obj['date'] = datetime.datetime.strptime(tdlist[2].text ,'%d/%m/%Y %H:%M:%S')
                obj['date'] = tdlist[2].text
                if len(tdlist[1].text) > 2:
                    obj['number'] = tdlist[1].text
                listone.append(obj)
            if soup.find(id='ctl00_cphPro_grdBillDetails_ctl13_btnNext'):
                nextb = driver.find_element_by_id('ctl00_cphPro_grdBillDetails_ctl13_btnNext')
                nextb.click()
                time.sleep(2)
            else:
                EndMonth = 1
                make_stats(listone)
    driver.quit()
    return listone

def make_stats(daList):
    data = {'sec':0, 'cost':0.0}
    for obj in daList:
        if obj['type'] == 'DATA':
            data['sec'] += obj['duration']
            data['cost'] += obj['cost']
        else:
            print obj
    print data

if __name__ == '__main__':
    daList = lycamobile()
    make_stats(daList)
    with open('my_json.txt', 'w') as fp:
        json.dump(daList, fp)
    fp.close()
