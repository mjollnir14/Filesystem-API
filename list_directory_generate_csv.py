import os
'''
    For the given path, get the List of all files in the directory tree 
'''


def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a file then add it to the list
        if os.path.isfile(fullPath):
            print("file found: ", fullPath)
            allFiles.append(entry)
    return allFiles


def main():

    dirName = '/home/ben/'

    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)

    # Print the files
    for elem in listOfFiles:
        print(elem)

if __name__ == '__main__':
    main()
