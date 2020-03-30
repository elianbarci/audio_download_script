from bs4 import BeautifulSoup
from selenium import webdriver

url = "http://bbcsfx.acropolis.org.uk/"
browser = webdriver.PhantomJS()
browser.get(url)
html = browser.page_source
print(html)
soup = BeautifulSoup(html, 'lxml')
a = soup.find('section', 'wrapper')