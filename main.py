from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq, Request
from defusedxml import lxml
import requests
import logging

a = input("Enter the product name: ")
amazon_url = "https://www.amazon.com/s?k=" + a
flipkart_url = "https://www.flipkart.com/search?q=" + a
jiomart_url = "https://www.jiomart.com/search/" + a
snapdeal_url = "https://www.snapdeal.com/search?keyword=" + a
hdr = {'User-Agent': 'Mozilla/5.0'}
# urlclient helps to fetch the data from the url
req=Request(amazon_url,headers=hdr)
urlClient = uReq(req)
req1=Request(flipkart_url,headers=hdr)
urlClient1 = uReq(req)
req=Request(jiomart_url,headers=hdr)
urlClient2 = uReq(req)
req=Request(snapdeal_url,headers=hdr)
urlClient3 = uReq(req)

# read helps to read the data from the url
html_data = urlClient.read()
html_data1 = urlClient1.read()
html_data2 = urlClient2.read()
html_data3 = urlClient3.read()

# bs helps to parse the data
amazon_soup = bs(html_data, 'html.parser')
flipkart_soup = bs(html_data1, 'html.parser')
jiomart_soup = bs(html_data2, 'html.parser')
snapdeal_soup = bs(html_data3, 'html.parser')

bigbox = amazon_soup.findAll("div", {"class": "sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16"})
bigbox1 = flipkart_soup.findAll("div", {"class": "_1AtVbE col-12-12"})
bigbox2 = jiomart_soup.findAll("div", {"class": "ais-InfiniteHits-item jm-col-4 jm-mt-base"})
bigbox3 = snapdeal_soup.findAll("div", {"class": "col-xs-6  favDp product-tuple-listing js-tuple"})

print(bigbox3)