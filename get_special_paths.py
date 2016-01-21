
import sys
import re
import os
import shutil
import commands

#creates list of files in parent directory
files = os.listdir('./')

#convert list of files to string
filesstring = str(files)

#locate 'special files' with [asd__asdfasd_asdf.as] as the formatting
specialfiles = re.findall('\w*__\w*__.\w*', filesstring)

#invoke for loop to return absolute path for each 'special' file
for files in specialfiles:
    paths = os.path.abspath(files)
    print paths

