#!/usr/bin/python

# utf-8 

import requests
from bs4 import BeautifulSoup
import codecs
import configparser


headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36"}

login_url = 'https://account.lycamobile.nl/login.aspx?lang=en'
credithistory_url = 'https://account.lycamobile.nl/TopUp/CdrReport.aspx?lang=en'

def get_credentials()
    config = configparser.ConfigParser()
    config.read('credential')
    username = config.get('username')
    username = config.get('password')
    print username,password
    return username,password



s = requests.Session()
s.headers.update(headers)
r = s.get(login_url)
soup=BeautifulSoup(r.content)
VIEWSTATE=soup.find(id="__VIEWSTATE")['value']
VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR")['value']
EVENTVALIDATION=soup.find(id="__EVENTVALIDATION")['value']
username,password = get_credentials()
login_data = {
        '__LASTFOCUS': '',
        '__EVENTTARGET':'',
        '__EVENTARGUMENT':'',
        '__VIEWSTATE':VIEWSTATE,
        '__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
        '__EVENTVALIDATION':EVENTVALIDATION,
        'ctl00$cphPro$txtMobileNumber': username,
        'ctl00$cphPro$txtPassword': password,
        'txtSearchControlSearch2':'Search+Lycamobile',
        'ctl00$ucHeader$hdfActiveLink':'7',
        'ctl00$ucHeader$hdfActiveSubLink':'',
        'ctl00$cphPro$txtMobileNumber_MDevice':'',
        'ctl00$cphPro$txtPassword_MDevice': password,
        'ctl00$cphPro$btnLogin':'Log+in'
}

t = s.post(login_url, login_data)
#f = codecs.open('/tmp/prova.html','w',encoding='utf8')
#f.write(t.text)
#f.close()

#soup=BeautifulSoup(t.content)

if 'Welcome to My Lycamobile,' in t.content:
    r = s.get(credithistory_url)
    ml = soup.find(id="ctl00_cphPro_ddlListPeriod")
    for m in ml:
        get_monthvalue(s, m['value'])
else:
    print "Login failed"
    sys.exit(2)

def get_monthvalue(s, month):
    r = s.get(credithistory_url)
    soup=BeautifulSoup(r.content)
    VIEWSTATE=soup.find(id="__VIEWSTATE")['value']
    VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR")['value']
    EVENTVALIDATION=soup.find(id="__EVENTVALIDATION")['value']
    data = {
            'ctl00$ScriptManager2':'ctl00$cphPro$upCrdDetails|ctl00$cphPro$btnSubmit',
            'txtSearchControlSearch2':'Search Lycamobile',
            'ctl00$ucHeader$hdfActiveLink':'7',
            'ctl00$ucHeader$hdfActiveSubLink':'',
            'ctl00$CustomerInfo1$HdnSecMSISDN':'',
            'ctl00$CustomerInfo1$txtAddFriendNumber':'',
            'ctl00$CustomerInfo1$hidBundleCode':'',
            'ctl00$CustomerInfo1$hidResBundleCode':'',
            'ctl00$CustomerInfo1$hidSequenceNo':'',
            'ctl00$CustomerInfo1$hidOBABundleCode':'',
            'ctl00$cphPro$ddlListPeriod': month,
            'ctl00$cphPro$hf_grd':'0',
            'ctl00$cphPro$grdBillDetails$ctl13$ddlPageSelector':'1',
            'ctl00$cphPro$hf_grdPan':'0',
            'ctl00$cphPro$btnShow':'',
            'ctl00$cphPro$hfListPeriod':'0',
            '__EVENTTARGET':'',
            '__EVENTARGUMENT':'',
            '__LASTFOCUS':'',
            '__VIEWSTATE': VIEWSTATE,
            '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
            '__EVENTVALIDATION': EVENTVALIDATION,
            '__ASYNCPOST':'true',
            'ctl00$cphPro$btnSubmit':'Submit'
    }
    t = s.post(login_url, login_data)


def parse_page(s, month, page):
    soup=BeautifulSoup(r.content)
    VIEWSTATE=soup.find(id="__VIEWSTATE")['value']
    VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR")['value']
    EVENTVALIDATION=soup.find(id="__EVENTVALIDATION")['value']
    page_data = {
            'ctl00$ScriptManager2':'ctl00$cphPro$upResult|ctl00$cphPro$grdBillDetails$ctl13$btnNext',
            'txtSearchControlSearch2':'Search Lycamobile',
            'ctl00$ucHeader$hdfActiveLink':'7',
            'ctl00$ucHeader$hdfActiveSubLink':'',
            'ctl00$CustomerInfo1$HdnSecMSISDN':'',
            'ctl00$CustomerInfo1$txtAddFriendNumber':'',
            'ctl00$CustomerInfo1$hidBundleCode':'',
            'ctl00$CustomerInfo1$hidResBundleCode':'',
            'ctl00$CustomerInfo1$hidSequenceNo':'',
            'ctl00$CustomerInfo1$hidOBABundleCode':'',
            'ctl00$cphPro$ddlListPeriod': month,
            'ctl00$cphPro$hf_grd':'0',
            'ctl00$cphPro$grdBillDetails$ctl13$ddlPageSelector':'1',
            'ctl00$cphPro$hf_grdPan':'0',
            'ctl00$cphPro$btnShow':'',
            'ctl00$cphPro$hfListPeriod':'0',
            '__EVENTTARGET': EVENTTARGET,
            '__EVENTARGUMENT':'',
            '__LASTFOCUS':'',
            '__VIEWSTATE': VIEWSTATE,
            '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
            '__EVENTVALIDATION': EVENTVALIDATION,
            '__ASYNCPOST':'true'
            }
