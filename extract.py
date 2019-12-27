import sys
import os
import subprocess
import time

args = sys.argv
torrentName = args[1]
directory = '/media/pi/My Passport/Torrents/Seeding/' + torrentName
tempDirectory = '/media/pi/My Passport/Torrents/Temp'
extensionsToRemove = ['.mkv', '.avi']
minutesToSleep = 60 * 60
hasExtracted = False
 
def getFilesInDirectory():
    for subdir, dirs, files in os.walk(directory):
        return files
 
def isRarFile(file):
    return getFileExtension(file) == '.rar'
 
def extractArchive(file):
    print('Extracting ' + file)
    
    tempExtractDir = str(time.time())
    goToTempDir = "cd '" + tempDirectory + "'"
    createTempExtractDir = "mkdir " + tempExtractDir
    goToTempExtractDir = goToTempDir + "/" + tempExtractDir
    extractRar = "7z e '" + directory + "/" + file + "'"
    moveFilesToDirectory = "mv * '" + directory + "'"
    removeTempExtractDir = "rmdir " + tempExtractDir
    
    subprocess.call(goToTempDir + ' && ' + createTempExtractDir, shell=True)
    subprocess.call(goToTempExtractDir + ' && ' + extractRar, shell=True)
    subprocess.call(goToTempExtractDir + ' && ' + moveFilesToDirectory, shell=True)
    subprocess.call(goToTempDir + ' && ' + removeTempExtractDir, shell=True)
 
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
    if isRarFile(file):
        hasExtracted = True
        extractArchive(file)
 
if hasExtracted == False:
    print('No files extracted, stopping...')
    exit()
 
print('Waiting for removal...')
time.sleep(minutesToSleep)
removeFiles()
