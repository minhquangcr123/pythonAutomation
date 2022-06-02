#!/bin/env python3

import os
import shutil



class CopyToDest:
    # list_file:    List file that you using to try to find and copy to dest
    # folder:       The folder that you want to look up
    # dest_path:    Path that you copy the file wanted to
    # TBD...
    def __init__ (self, list_file, src_path, dest_path):
        self.list_file = list_file
        self.src_path = src_path
        self.dest_path = dest_path
        self.log_file_have_copied = []

    def copyFile(self):
        print('Find the specific file and copy to the destination folder!\n ----------- List file: ')
        for fileNeedDelete in self.list_file:
            print ('\t->' + fileNeedDelete)

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
                    print('Have find out a file need to copy in the list! : ' + self.src_path)
                    try:
                        shutil.copy(self.src_path, self.dest_path)
                    except shutil.SameFileError:
                        pass
                    self.log_file_have_copied.append(self.src_path)      

    def deleteFileCopy(self, folder):
        file_avoid = [__file__, "TBD.txt"]

        

        for file in os.listdir(folder):
            if file in self.list_file:
                print("Delete {} from".format( file ) + folder)
                file_path = os.path.join(folder, file)
                os.remove(file_path)

    def writeLogToFile(self, file_log):
        print("Write log source path to file!")
        with open(file_log, 'w') as file:
            for source_path in self.log_file_have_copied:
                file.write(source_path + '\n')

    def printFileLog(self):
        for source_path in log_file_have_copied:
            print ('{} \n'.format(source_path))



if __name__ == '__main__':

    # folder_build = r'D:\PROJECT\Intergrator\mono_radar_learning\build'
    # folder_ipif = r'D:\PROJECT\Intergrator\mono_radar_learning\ip_if'
    folder_test = r'/home/tranquang/Desktop/project/automation/copySpecificFile'

    # dest_path = r'D:\PROJECT\Competences\AutomationTool'
    dest_test = r'/home/tranquang/Desktop/project/automation/copySpecificFile/test/testcopy'

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

    copyObj = CopyToDest(list_file, folder_test, dest_test) 
    copyObj.deleteFileCopy(dest_test)
    copyObj.copyFile()
    # copyObj.writeLogToFile('log.txt')
