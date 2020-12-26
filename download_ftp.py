import  os
from ftplib import FTP
try:
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect('10.50.21.100',21212)
    ftp.login('ics_vul','dbapp@2018')
    buf_size = 1024
    filename = "test1.cpp"
    f = open(filename,'wb')
    ftp.retrbinary('RETR test.cpp', f.write, buf_size)
    ftp.quit()
    f.close()
except Exception as e:
    print (e)
