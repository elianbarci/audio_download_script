from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import time

folderID = ""
FileList = []

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

def checkElementsIfElementIsAlreadyLoaded(name_of_file, fileList):

    global FileList
    returntype = True

    if(len(fileList)==0):
        FileList = fileList
        return returntype

    else:

        if(len(FileList) != 0):
            fileList = FileList

        for fileaux in fileList:
            if(fileaux['title'] == name_of_file):
                fileList.remove(fileaux)
                returntype = False
                FileList = fileList
                return returntype
            else:
                pass
    
    return returntype

def getFileList(fileID, drive):
    query = "'" + fileID + "' in parents and trashed=false"
    fileList = drive.ListFile({'q': query}).GetList()
    return fileList

def getNewFileList():
    global FileList
    return FileList