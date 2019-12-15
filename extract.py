import sys
import os
import time
import zipfile
 
args = sys.argv
torrentName = args[1]
directory = '/media/pi/My Passport/Torrents/Seeding/' + torrentName
extensionsToExtract = ['.zip', '.rar']
extensionsToRemove = ['.mkv', '.avi']
minutesToSleep = 15 * 60
hasExtracted = False
 
def getFilesInDirectory():
    for subdir, dirs, files in os.walk(directory):
        return files
 
def isZipOrRarFile(file):
    return getFileExtension(file) in extensionsToExtract
 
def extractArchive(file):
    print('Extracting ' + file)
    with zipfile.ZipFile(directory + '/' + file, 'r') as zf:
        for item in zf.namelist():
            try:
                zf.extract(item, path=directory)
                print('Extracted ' + item)
            except:
                print('Could not extract ' + item)
 
def removeFiles():
    for file in getFilesInDirectory():
        if getFileExtension(file) in extensionsToRemove:
            print('Removed ' + file)
            os.remove(directory + '/' + file)
 
def getFileExtension(file):
    return os.path.splitext(file)[1]
 
if os.path.isfile(directory):
    print('Directory path is a file, stopping...')
    exit()
 
for file in getFilesInDirectory():
    if isZipOrRarFile(file):
        hasExtracted = True
        extractArchive(file)
 
if hasExtracted == False:
    print('No files extracted, stopping...')
    exit()
 
print('Waiting for removal...')
time.sleep(minutesToSleep)
removeFiles()
