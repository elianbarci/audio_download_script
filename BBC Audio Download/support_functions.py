from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

folderID = ""

def getGoogleDriveInstance():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

def stablishGoogleDriveFolder(drive, name_of_folder):
    fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file in fileList:
        if(file['title'] == name_of_folder):
            global folderID 
            folderID = file['id']
            return folderID

def checkElementsIfElementIsAlreadyLoaded(drive, name_of_file):  
    global folderID 
    query = "'" + folderID + "' in parents and trashed=false"
    fileList = drive.ListFile({'q': query}).GetList()
    if(len(fileList)==0):
        return True
    for fileaux in fileList:
        if(fileaux['title'] == name_of_file):
            print("El elemento " + fileaux['title'] + " ya estaba en la carpeta de Google Drive")
            return False
    return True