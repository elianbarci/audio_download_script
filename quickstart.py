from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))
  if(file['title'] == "TestUpload"):
      fileID = file['id']

file1 = drive.CreateFile({"mimeType": "audio/*", "parents": [{"kind": "drive#fileLink", "id": fileID}]})
file1.SetContentFile("wav_links.txt")
file1.Upload()
print('Created file %s with mimeType %s' % (file1['title'], file1['mimeType']))   

