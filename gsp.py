import sys
import re
import os
import shutil
import commands

def get_special_paths(dir):
    
#this function accepts a directory as an argumentand returns the absolute paths of any
#files formated like this: asdf__asdfa__.asd


    #creates list of files in parent directory
    files = os.listdir(dir)

    #converts list of files to string
    filesstring = str(files)

    #locates 'special files' with [asd__asdfasd_asdf.as] as the formatting
    specialfiles = re.findall('\w*__\w*__.\w*', filesstring)

    #invokes for loop to print absolute path for each 'special' file
    for files in specialfiles:
        paths = os.path.abspath(files)
        return paths

def copy_to(files, directory):
    shutil.copy(files, directory)


#for files in paths:
#    copy_to(files, '/Users/Lauren')

def main(directoryname):
    get_special_paths(directoryname)

    

