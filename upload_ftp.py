import  os
from ftplib import FTP
try:
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect('10.50.21.100',21212)
    ftp.login('ics_vul','dbapp@2018')
    buf_size = 1024
    filename = "./test.cpp"
    f = open(filename,'rb')
    ftp.storbinary('STOR ' + os.path.basename(filename), f, buf_size)
    f.close()
    ftp.quit()
except Exception as e:
    print (e)