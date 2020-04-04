from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

soups = []
driver = webdriver.Chrome()
driver.get('http://bbcsfx.acropolis.org.uk/')
page = 0
time.sleep(5)

while page < 1:
    soups.append(BeautifulSoup(driver.page_source))
    page = page + 1
    driver.get('http://bbcsfx.acropolis.org.uk/?page=' + str(page))
    time.sleep(5)

driver.quit
file1 = open("wav_links.txt","w")
filename = ""

for soup in soups:

    tags =  soup('audio')
<<<<<<< Updated upstream
    description = soup.findAll('td', {'tabindex': '0'})
    aux_description = 0
    
=======
    

>>>>>>> Stashed changes
    for tag in tags:
        file1.write('http://bbcsfx.acropolis.org.uk' + tag.get('src')[2:] + " " +  description[aux_description].getText() + "\n")
        print("Se comenzo a descargar el archivo: " + description[aux_description].getText())
        r = requests.get('http://bbcsfx.acropolis.org.uk' + tag.get('src')[2:])
        filename = description[aux_description].getText()

        with open(filename, 'wb') as f:
            f.write(r.content)
            print("Se descargo correctamente el archivo: " + filename)

        file_upload = drive.CreateFile({"mimeType": "audio/*", "parents": [{"kind": "drive#fileLink", "id": fileID}]})
        file_upload.SetContentFile(filename)
        try:
            file_upload.Upload()
        finally:
            file_upload.content.close()
        if file_upload.uploaded: 
            print("Se subio correctamente el archivo: " + filename)
            try:
                os.remove(filename)
                print(" El archivo fue eliminado correctamente") 
            except OSError:
                print(" El archivo fue eliminado incorrectamente") 
                pass

        aux_description =  aux_description + 1
