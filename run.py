import urllib.request

__version__ = "1.0.0"
__author__ = "Luka Pavicic"

def checkHumble():
    print("Humble Bundle FREE games checker. Made by Luka Pavicic")

    htmlCodeFile = open("humblebundlesourcecode.txt","w")
    url = "https://www.humblebundle.com"
    # request read
    print("Sending request to {}".format(url))
    request = urllib.request.urlopen(url)
    print("Request sent to {}".format(url))
    requestRead = request.read()
    requestRead = str(requestRead)
    htmlCodeFile.write(requestRead)
    htmlCodeFile.close()

    # check request
    print("Opening source code file...")
    htmlCodeFileRead = open("humblebundlesourcecode.txt","r")
    print("Source code file opened...")
    print("Reading from the file...")
    htmlCodeFileReadDone = htmlCodeFileRead.read()
    print("Reading file finished")
    htmlCodeFileReadDone = str(htmlCodeFileReadDone)
    # print result
    print("----------------------RESULT------------------------")
    if('"amount": 0.00' in htmlCodeFileReadDone or "FREE" in htmlCodeFileReadDone):
        print("There is FREE game on Humble Bundle!")
    else:
        print("No free games on Humble Bundle today!")

    htmlCodeFileRead.close()

checkHumble()
input()


