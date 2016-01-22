
import sys
import re
import os
import shutil
import commands
import gsp

#requests directory as input and runs the gsp function on the dir

directory = input('What Directory: ')

gsp.get_special_directory(directory)    
