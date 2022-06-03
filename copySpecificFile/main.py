#!/bin/env python3

import os
import shutil

# For color in command promt
os.system("")

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
        print(bcolors.FAILT + message + bcolors.ENDC)

class CopyToDest:
    # list_file:    List file that you using to try to find and copy to dest
    # folder:       The folder that you want to look up
    # dest_path:    Path that you copy the file wanted to
    # TBD...
    def __init__ (self, list_file, dest_path):
        self.list_file = list_file
        self.src_path = ' '
        self.dest_path = dest_path
        self.log_file_have_copied = []

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
        print ('\t->' + self.dest_path + '\n')

    def copyFile(self, folder):
        print('Find the specific file and copy to the destination folder!')
        self.src_path = folder
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
                if fileName in self.list_file:
                    displayException('Have find out a file need to copy in the list - ' + self.src_path)
                    try:
                        shutil.copy(self.src_path, self.dest_path)
                    except shutil.SameFileError:
                        pass
                    self.log_file_have_copied.append(self.src_path)      

    def deleteFileCopy(self, folder):
        file_avoid = [__file__, "TBD.txt"]
        try: # Make sure the folder exist
            files = os.listdir(folder)
            for file in os.listdir(folder):
                if file in self.list_file:
                    displayException("Delete {} from ".format( file ) + folder, STATUS.WARNING)
                    file_path = os.path.join(folder, file)
                    os.remove(file_path)
                
        except:
            displayException("Do not have the folder {}".format(folder))
       

    def writeLogToFile(self, file_log):
        log_file_path = os.path.join(self.dest_path, file_log)
        displayException("Write log source path to file : {}".format(log_file_path))
        
        with open(log_file_path, 'w') as file:
            for source_path in self.log_file_have_copied:
                file.write(source_path + '\n')

    def printFileLog(self):
        for source_path in log_file_have_copied:
            print ('{} \n'.format(source_path))



if __name__ == '__main__'   :

    folder_build = r'D:\PROJECT\Intergrator\mono_radar_learning\build'
    folder_ipif = r'D:\PROJECT\Intergrator\mono_radar_learning\ip_if'
    folder_test = r'D:\PROJECT\Competences\pythonAutomation\copySpecificFile\test'

    # dest_path = r'D:\PROJECT\Competences\AutomationTool'
    dest_test = r'D:\PROJECT\Competences\pythonAutomation\copySpecificFile\forCopyTo'

    log_file_have_copied = []
    current_dir = r'.'

    list_file = [
                    'test.txt',
                    'Dem_Cfg_DTC_DataStructures.c', 
                    'Dem_Cfg_DtcId.h', 
                    'Dem_Cfg_EventId.h',
                    'Fee_EcucValuesPro.arxml',  
                    'Fee_Report.txt',  
                    'Fls_Report.txt',  
                    'NvM_Report.txt',   
                    'rba_DemBfm.properties', 
                    'Dem.properties',  
                ]
    # Copy file, delete file, write log file
    copyObj = CopyToDest(list_file, dest_test) 
    copyObj.printInfor()
    copyObj.copyFile(folder_build)
    copyObj.writeLogToFile('log.txt')
    copyObj.deleteFileCopy(r'D:\PROJECT\Competences\pythonAutomation\copySpecificFile\forCopyTo')
    