#!/bin/env python3

import os
import sys
import shutil
import argparse
from ConfigParser import ConfigParser

# For color in command promt
os.system("")

config_file = r'copyFile.ini'
list_file = []
source_path = ''
dest_path = ''
include = []
exclude = []

class STATUS:
    SUCCESS=0
    WARNING=1
    ERROR=2

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def displayException(message, number=STATUS.SUCCESS):
    if number == 0:
        print(bcolors.OKGREEN + message + bcolors.ENDC)

    if number == 1:
        print(bcolors.WARNING + message + bcolors.ENDC)
    if number == 2:
        print(bcolors.FAIL + message + bcolors.ENDC)

class CopyToDest:
    # list_file:    List file that you using to try to find and copy to dest
    # folder:       The folder that you want to look up
    # dest_path:    Path that you copy the file wanted to
    # TBD...
    def __init__ (self, list_file):
        self.list_file = list_file
        self.src_path = ''
        self.dest_path = ''
        self.include = []
        self.exclude = []
        self.log_file_have_copied = []

    def setSourcePath(self, folder):
        self.src_path = folder

    def setDestPath(self, folder):
        self.dest_path = folder

    def setInclude(self, incl):
        self.include = incl 
    def setExclude(self, exc):
        self.exclude = exc

    def printInfor(self):
        print('Display some information :')
        # Print list file
        print('---------------- List file want to copy: ')
        for fileNeedDelete in self.list_file:
            print ('\t->' + fileNeedDelete)
            
        # Folder to find
        print('---------------- Source Path: ')
        print ('\t->' + self.src_path)

        # Folder copy to
        print('---------------- Destination Path: ')
        print ('\t->' + self.dest_path)
        
        # Folder copy to
        print('---------------- include: ')
        print ('\t-> {} \n'.format(self.include))

        # Folder copy to
        print('---------------- exclude: ')
        print ('\t-> {} \n'.format(self.exclude))

    def copyFile(self):
        print('Find the specific file and copy to the destination folder!')
        # Recursive find the file in list from the wanted folder
        # fileNames = os.listdir(self.src_path)
        # for fileName in fileNames:
        #     self.src_path = os.path.abspath(os.path.join(self.src_path, fileName))
        #     print('File with path : ' + self.src_path + '\n')
        #     if fileName in self.list_file:
        #         print('Have find out a source in the list!')
        #         shutil.copy(self.src_path, self.dest_path)
        #         self.log_file_have_copied.append(src_path)      
        #     else:
        #         if os.path.isdir(self.src_path):
        #             self.copyFile()

        for root, dirs, files in os.walk(self.src_path):    
            for fileName in files:
                self.src_path = os.path.abspath(os.path.join(root, fileName))
                if ((fileName in self.list_file) and any(x in self.src_path for x in self.include) and all(ex not in self.src_path for ex in self.exclude)): # \
                    try:
                        shutil.copy(self.src_path, self.dest_path)
                        displayException('Have find out a file need to copy in the list - ' + self.src_path)
                    except shutil.Error:
                        pass
                    self.log_file_have_copied.append(self.src_path)      
                    # displayException('Can not find the file {}'.format(fileName))

    def cleanDestPath(self):
        file_avoid = [__file__, "TBD.txt"]
        try: # Make sure the self.dest_path exist
            for files in os.listdir(self.dest_path):
                if files in self.list_file:
                    displayException("Delete from {}, file delete: ".format( self.dest_path ) + files, STATUS.WARNING)
                    file_path = os.path.join(self.dest_path, files)
                    os.remove(file_path)
                
        except:
            displayException("Do not have the destination path - Some thing wrong".format(self.dest_path))
       

    def writeLogToFile(self, file_log):
        log_file_path = os.path.join(self.dest_path, file_log)
        displayException("Write log source path to file : {}".format(log_file_path))
        
        with open(log_file_path, 'w') as file:
            for source_path in self.log_file_have_copied: 
                file.write(source_path + '\n')

    def printFileLog(self):
        for source_path in log_file_have_copied:
            print ('{} \n'.format(source_path))

    
def readConfig(config_file, s_item):
    config = ConfigParser()
    config.read(config_file)
    key_item = config.items(s_item)
    return key_item

def updateConfig():
    print("Parse argument pass to the python script!")
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type = str, help ='A required config path')
    parser.add_argument('--source', type = str, help ='A required soruce path')
    parser.add_argument('--dest', type = str, help ='A required dest path')
    parser.add_argument('--include', nargs="+", help ='<word>  to include for finding')
    parser.add_argument('--exclude', nargs="+", help ='<word>  to exclude for finding')
    args = parser.parse_args()

    # Update config, source ,dest
    global config_file
    global list_file
    global source_path
    global dest_path
    global include
    global exclude

    config_file = args.config
    if args.source:
        source_path = args.source
    if args.dest:
        dest_path = args.dest
    if args.include:
        include  = args.include 
    if args.exclude:
        exclude = args.exclude
    
def runCopy(source, dest, list_file, include, exclude):
    # Copy file, delete file, write log file
    copyObj = CopyToDest(list_file) 
    copyObj.setSourcePath(source)
    copyObj.setDestPath(dest)
    copyObj.setInclude(include)
    copyObj.setExclude(exclude)
    copyObj.printInfor()
    copyObj.cleanDestPath()     
        
    copyObj.copyFile()
    # copyObj.writeLogToFile('log_of_copy.txt')



def main():  
    # Parse list file
    global config_file
    global list_file
    global source_path
    global dest_path
    global include
    global exclude

    if (len(sys.argv) > 3) and ('--config' in sys.argv):
        print('Update config file!')
        updateConfig()
        for key,item in readConfig(config_file, 'list_file'):
            list_file.append(item)

        runCopy(source_path, dest_path, list_file, include, exclude)

    elif (len(sys.argv) > 1) and ('--config' in sys.argv):
        updateConfig()
        print('Using default config file!')

        for key,item in readConfig(config_file, 'list_file'):
            list_file.append(item)

        for key,item in readConfig(config_file, 'paths'):
            if key == 'source':
                source_path = item  
            elif key == 'dest':
                dest_path = item

        for key,item in readConfig(config_file, 'include'):
            include.append(item)
        for key,item in readConfig(config_file, 'exclude'):
            exclude.append(item)
        
        runCopy(source_path, dest_path, list_file, include, exclude)

    else:
        displayException("Please enter the --config <path_to_.ini> ", STATUS.ERROR)
        updateConfig()
        sys.exit(1)

    sys.exit(0)

if __name__ == '__main__'   :
    main()

    
 