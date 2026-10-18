

import urllib.request

def download(tutorialName):
    url = 'https://www.tutorialspoint.com/' + tutorialName + '/' + tutorialName + '_tutorial.pdf'
    downloadLocation = '/home/vinayak/Downloads/'

    pdf = urllib.request.urlopen(url)
    saveFile = open(downloadLocation + tutorialName +  '.pdf', 'wb')                                
    saveFile.write(pdf.read())
    saveFile.close()
    print('Downloaded!')

if __name__ == '__main__':
    tutorialName = input('Name of the tutorial pdf to be downloaded: ')
    download(tutorialName)
