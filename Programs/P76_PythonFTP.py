
                                                                                      
                                               
                                
                         
                                                   
                               

                                                 
 
                                                            
                                         
                                                                     
                                                                             
                                                                                                   
                                                                                     
                                                                                                           
                                                                 
                                                                 
                                                                                        
                                                                           
                                                                           
                                            

import ftplib

def ftp_upload(ftpObj, pathToSend, pathToRecv, fileType='TXT'):
    """
    A function for uploading files to an FTP server
    @param ftpObj: The file transfer protocol object
    @param path: The path to the file to upload
    """
    with open(pathToSend, 'rb') as fobj:
        ftpObj.storlines('STOR ' + pathToRecv, fobj)

if __name__ == '__main__':
    ftp = ftplib.FTP('127.0.0.1')
    ftp.login('vinayak', '8149VinayakYadav')
    print('Logged in..')

    pathToSend = '/home/vinayak/Desktop/output.txt'
    pathToRecv = '/home/vinayak/Documents/output.txt'
    ftp_upload(ftp, pathToSend, pathToRecv)

    ftp.quit()
