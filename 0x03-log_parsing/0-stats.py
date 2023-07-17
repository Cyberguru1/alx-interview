#!/usr/bin/python3

import sys


count = 0
fileSize = 0
statusCodes = [200, 301, 400, 401, 403, 404, 405, 500]
mappings =  {i:0 for i in statusCodes}

def print_mappings():
    """
    Methond to print the mappings
    Args:
         None
    Returns:
         None
    """
    print("File size: {}".format(fileSize))
    for i in mappings:
        if mappings[i] == 0:
            continue
        print(f"{i}: {mappings[i]}")


while (out:=sys.stdin.readline()):
    try:
        splited = out.strip().split(" ")
        sCode = int(splited[-2])
        fSize = splited[-1]

        if sCode in statusCodes:

            if sCode in mappings:
                mappings[sCode] += 1
            else:
                mappings[sCode] = 1

        if count == 10:
            print_mappings()
            count = 0

        count += 1
        fileSize += int(fSize)
    except KeyboardInterrupt:
        print_mappings()
