#!/usr/bin/python

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import sys, time
import datetime
import json
import codecs

from elasticsearch import Elasticsearch


fr = open("cc",'r')
html_source = fr.read()
fr.close()
soup = BeautifulSoup(html_source, 'html.parser')
table = soup.findAll(id="receivedTransactions")[0]
tbody = table.findAll("tbody")[1]
total = []
for tr in tbody.findAll("tr"):
    exp_list = tr.findAll("td")
    singlee = {}
    if len(exp_list) > 1:
        #date
        if exp_list[0].text != "":
            # datetime.datetime.strptime(exp_list[0].text, '%d-%m-%Y')
            singlee['when'] = exp_list[0].text
            singlee['pub_date'] = datetime.datetime.strptime(exp_list[0].text, '%d-%m-%Y').strftime('%Y-%m-%dT%H:%M:%S')
        details = exp_list[1].findAll("div")
        if len(details) > 12:
            # what i.e. AH
            singlee['what'] = details[0].text
            # transaction
            singlee['trans'] = details[1].text
            # Mutatiesoort
            singlee['st1'] = details[4].text
            # BA
            singlee['type'] = details[5].text
            # Mededelingen
            singlee['st2'] = details[7].text
            # Transactie:32K5Q6 Term:605Q60 
            singlee['trans'] = details[11].text
            # Amount
            ll = exp_list[3].text.split(' ')
            singlee['amount'] = float(ll[0].replace('.','').replace(',','.'))
            singlee['dir'] = ll[-1]
            if singlee['dir'] != 'Af':
                singlee['value'] = singlee['amount'] * -1
            else:
                singlee['value'] = singlee['amount']
    total.append(singlee)
fw = codecs.open("cc.json", 'w', encoding='utf8')
fw.write(json.dumps(total))
fw.close()
es = Elasticsearch(['localhost:9200'])
for doc in total:
    res = es.index(index="test-index", doc_type='entry', body=doc)
    print(res['created'])

es.indices.refresh(index="test-index")

