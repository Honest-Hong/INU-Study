#-*- coding: utf-8 -*_
import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()

page = raw_input("plz input word : ")

url = 'https://ko.wikipedia.org/wiki/' + str(page)
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'html.parser')
for link in soup.select('p > b'):
    title = link.string
    if u"������ ��������" in title:
        print("�������� �ʴ� �ܾ��Դϴ�.")
        break;
    else:
        print("�����ϴ� �ܾ� �Դϴ�.")
        break;