
#!/bin/env python3

import os
import shutil

list_file = [
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

folder_build = r'D:\PROJECT\Intergrator\mono_radar_learning\build'
folder_ipif = r'D:\PROJECT\Intergrator\mono_radar_learning\ip_if'

src_path = ''
dest_path = r'D:\PROJECT\Competences\AutomationTool'
log_file_have_copied = []
current_dir = r'.'

def listDir(dir):
    print('Try to find something!')
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        src_path = os.path.abspath(os.path.join(dir, fileName))
        print('File with path : ' + src_path + '\n')

        if fileName in list_file:
            print('Have find out a source in the list!')
            shutil.copy(src_path, dest_path)
            log_file_have_copied.append(src_path)      
        else:
            if os.path.isdir(src_path):
                listDir(src_path)

def cleanDir(dir):
    print("Clean curent dir!")
    for f in os.listdir(dir):
        if f == __file__:
            continue
        os.remove(os.path.join(dir, f))

def writeLogToFile(file_log):
    print("Write log source path to file!")
    with open(file_log, 'w') as file:
        for source_path in log_file_have_copied:
            print ('{} \n'.format(source_path))
            file.write(source_path + '\n')

def printLog():
    print("Print log for checking again!")
    for source_path in log_file_have_copied:
        print ('{} \n'.format(source_path))

if __name__ == '__main__':
    cleanDir(current_dir)

    listDir(folder_build)
    listDir(folder_ipif)

    writeLogToFile('log_file_copied.txt')   
    