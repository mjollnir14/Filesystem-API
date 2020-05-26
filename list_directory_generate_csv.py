'''
    For the given path, get the List of all files in the directory tree 
'''

import os
import csv

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a regular file and if match extension then add it to the list
        if os.path.isfile(fullPath) and entry.endswith(".mp4"):
            print("file found: ", fullPath)
            allFiles.append(entry)
    return allFiles


def main():

    dirName = '/home/ben/test'

    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)

    # Print the files
    for elem in listOfFiles:
        print(elem)

    with open('content.csv', mode='w') as output_file:
        content_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Headers
        content_writer.writerow(['filename', 'creation'])

        # Data
        for elem in listOfFiles:
            content_writer.writerow([elem, '1970-01-01'])

if __name__ == '__main__':
    main()
