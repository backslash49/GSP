
#this function accepts a directory as an argumentand returns the absolute paths of any
#files formated like this: asdf__asdfa__.asd

import sys
import re
import os
import shutil
import commands

def gsp(dir):
    #creates list of files in parent directory
    files = os.listdir(dir)

    #converts list of files to string
    filesstring = str(files)

    #locates 'special files' with [asd__asdfasd_asdf.as] as the formatting
    specialfiles = re.findall('\w*__\w*__.\w*', filesstring)

    #invokes for loop to print absolute path for each 'special' file
    for files in specialfiles:
        paths = os.path.abspath(files)
        print paths

