#!/usr/bin/python3

import os
import zipfile

def verifyzip(fileName):
    fileExt = ".zip"
    stop = 4
    fileSlice = slice(stop)
    iszip = fileName[fileSlice]
    print(iszip)
    





def amin():
    fileName = input("What is the file nae? ")
    if os.path.exists(fileName):
        print("That file does exist")
    else:
        print("That file does not exist")

    verifyzip(fileName)

    main()
