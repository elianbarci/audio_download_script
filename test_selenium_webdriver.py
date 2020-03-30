from selenium import webdriver
from bs4 import BeautifulSoup
import time

soups = []
driver = webdriver.Chrome()
driver.get('http://bbcsfx.acropolis.org.uk/')
page = 0
time.sleep(5)

while page < 12:
    soups.append(BeautifulSoup(driver.page_source))
    page = page + 1
    driver.get('http://bbcsfx.acropolis.org.uk/?page=' + str(page))
    time.sleep(5)

driver.quit
#links = []
file1 = open("wav_links.txt","w")

for soup in soups:
    tags =  soup('audio')
    for tag in tags:
        #links.append('http://bbcsfx.acropolis.org.uk' + tag.get('src')[2:] + "\n")#Slice syntax give me the part of this sequence which begins at index 2 and continues to the end (since no end point was specified after the colon)
        file1.write('http://bbcsfx.acropolis.org.uk' + tag.get('src')[2:] + "\n")

file1.close()
