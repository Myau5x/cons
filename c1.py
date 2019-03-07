## https://washington.mid.ru/ru/consular-services/consulate/consul_sessions/

'''
Try to parse info about counsil session
'''

import requests
from bs4 import BeautifulSoup
import sys

URL = 'https://washington.mid.ru/ru/consular-services/consulate/consul_sessions/'

def check_sd(url_cons, pattern):
    """
    Check that page with URL is the same as pattern
    """
    responce = requests.get(url_cons)
    html = responce.content
    soup = BeautifulSoup(html,'html.parser')
    url_page = soup.select_one('div.page')
    with open(pattern,'r') as f:
        html2 = f.read()
        pat_page = BeautifulSoup(html2,'html.parser').select_one('div.page')
    return url_page != pat_page

if __name__ == "__main__":
    pat  = sys.argv[1]
    change  = check_sd(URL,pat)
    if  change:
        print('Panic!!!! Consul change something!')
    else:
        print('all same')
