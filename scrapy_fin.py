import scrapy
import requests
from pandas import DataFrame
import json

url = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=1nzf&st=desc&sd=2018-10-28&ed=2019-10-28&qdii=&tabSubtype=,,,,,&pi=1&pn=5&dx=1&v=0.7671072158682894'
res = requests.get(url)
content = res.text
print(content)

fix_res = content[14:]
fix_res = fix_res[:-1]

print(fix_res)