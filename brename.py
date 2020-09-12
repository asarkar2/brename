#!/usr/bin/env python

import sys
import os
from os.path import basename

# Read lines of the file to an array
def readfile(filename):
    
    with open(filename) as f:
        content = f.readlines()
    
    # Remove whitespace characters and '\n' at the end of each line
    content = [x.strip() for x in content] 

    # Remove blank empty lines
    content = filter(None, content)

    return content

# Helptext
def helptext(scriptname):
    
    print("Script to bulk rename files from input list to output list.")
    print("Usage: %s [options] -i list1 -o list2" % scriptname)
    print("Options:")
    print("-h|--help        Show this help and exit.")

    return

# Main program starts
if __name__ == '__main__':
    
    scriptname = basename(sys.argv[0])

    # Number of arguments supplied via cli
    numargv = len(sys.argv)-1
    # Argument count
    iargv = 1

    # Parse cli options
    while iargv <= numargv:
        
        if sys.argv[iargv] == "-h" or sys.argv[iargv] == "--help":
            helptext(scriptname)
            sys.exit()        

        elif sys.argv[iargv] == "-i":
            file1 = sys.argv[iargv+1]
            iargv += 1

        elif sys.argv[iargv] == "-o":
            file2 = sys.argv[iargv+1]
            iargv += 1

        else:
            print ("%s: Unspecified option: '%s'. Aborting."
                % (scriptname, sys.argv[iargv]))
            sys.exit(1)

        iargv += 1


    # Read the lines of the files to list
    content1 = readfile(file1)
    content2 = readfile(file2)

    # Check the number of files
    if len(content1) != len(content2):
        print("Number of lines are not same. Aborting.")
        sys.exit(1)

    # Iteration counter
    i = 0

    # Iterate over files
    for line1 in content1:

        # Check if files exist or not
        if not os.path.exists(line1):
            print("File '%s' doesn't exist. Aborting." % line1)
            sys.exit(1)

        # New filename
        line2 = content2[i]

        # Check if old and new filenames are same or not
        if line1 == line2:
            print("Filenames are same for: '%s'" % line1)

        # If filenames are different, rename them
        else:
            os.rename(line1,line2)
            print("'%s' -> '%s'" %(line1, line2))

        # Increase iteration 
        i = i + 1 

