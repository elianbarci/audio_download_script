from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import os
import re
import support_functions
import sys

drive = support_functions.getGoogleDriveInstance()
fileID = support_functions.stablishGoogleDriveFolder(drive, "TestUpload")
fileList = support_functions.getFileList(fileID, drive)

soup = []
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://bbcsfx.acropolis.org.uk/')
page = 1

while page < 621:

    driver.quit
    time.sleep(5)
    filename = ""
    soup = BeautifulSoup(driver.page_source, "html.parser")
    tags = soup('audio')
    description = soup.findAll('td', {'tabindex': '0'})
    aux_description = 0

    for tag in tags:

        filename = ""
        filename = description[aux_description].getText()
        filename = re.sub('[!@#$./\?%*:|"<>]', '', filename)

        if(support_functions.checkElementsIfElementIsAlreadyLoaded(filename, fileList) == True):

            fileList = support_functions.getNewFileList()

            print("Se comenzo a descargar el archivo: " + filename)

            r = requests.get(
                'http://bbcsfx.acropolis.org.uk' + tag.get('src')[2:])

            with open(filename, 'wb') as f:
                f.write(r.content)
                print("Se descargo correctamente el archivo: " + filename)

            file_upload = drive.CreateFile(
                {"mimeType": "audio/*", "parents": [{"kind": "drive#fileLink", "id": fileID}]})

            file_upload.SetContentFile(filename)

            try:
                file_upload.Upload()
            finally:
                file_upload.content.close()

            if file_upload.uploaded:

                print("Se subio correctamente el archivo: " + filename)

                try:
                    os.remove(filename)
                    print("El archivo: fue eliminado correctamente")
                except OSError:
                    print("El archivo fue eliminado incorrectamente")
                    pass

        aux_description = aux_description + 1

    page = page + 1
    driver.get('http://bbcsfx.acropolis.org.uk/?page=' + str(page))

print("Finalizo correctamente")
