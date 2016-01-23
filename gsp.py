import sys
import re
import os
import shutil
import commands

def get_special_paths(dir):
    
#this function accepts a directory as an argumentand returns the absolute paths of any
#files formated like this: asdf__asdfa__.asd

    result = []
    
    #creates list of files in named directory
    files = os.listdir(dir)

    #converts list of files to string
    filesstring = str(files)

    #locates 'special files' with [asd__asdfasd_asdf.as] as the formatting
    specialfiles = re.findall('\w*__\w*__.\w*', filesstring)

    #invokes for loop to print absolute path for each 'special' file
    for files in specialfiles:
        result.append(os.path.abspath(os.path.join(files)))
    return result


#    shutil.copy(files, '/Users/lauren/Downloads/google-python-exercises')

    
#for files in paths:
#    copy_to(files, '/Users/Lauren')


def copy_to(specialfilepaths, directory):
    if not os.path.exists(directory): #creates directory if it doesnt exist
        os.mkdir(directory)
    for path in specialfilepaths:   #runs for loop on files in specialfilepaths       
        shutil.copy(path, os.path.join(directory)) #copies to directory

def main():
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
        sys.exit(1)
    todir = '' #tudir = where its going
    if args[0] == '--todir':
        todir = args[1] #defining tudir from cmd line
        del args[0:2] 
    if len(args) == 0:
        print "error: must specify one or more directories"
        sys.exit(1)

    paths = [] #blank list to be populated with with special filenames
    dirname = sys.argv[3] #input location for special files
    paths.extend(get_special_paths(dirname)) #creating list of special files in 
    if todir:
        copy_to(paths, todir)
    
    
#    initiates main() function on cmd line, if present in function
if __name__ == "__main__":
  main()

