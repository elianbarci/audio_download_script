from selenium import webdriver
from bs4 import BeautifulSoup
import time, requests, os, re, support_functions

drive = support_functions.getGoogleDriveInstance()
fileID = support_functions.stablishGoogleDriveFolder(drive, "TestUpload")

soup = []
driver = webdriver.Chrome()
driver.get('http://bbcsfx.acropolis.org.uk/')
page = 1
time.sleep(5)

while page < 621:

    soup.append(BeautifulSoup(driver.page_source))
    time.sleep(5)
    driver.quit
    filename = ""
    tags = soup[page]('audio')
    description = soup[page].findAll('td', {'tabindex': '0'})
    aux_description = 0

    for tag in tags:

        filename = description[aux_description].getText()
        filename = re.sub('[!@#$./\?%*:|"<>]', '', filename)

        if(support_functions.checkElementsIfElementIsAlreadyLoaded(drive, filename)):

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
