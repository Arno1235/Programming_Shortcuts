from keyboardFunctions import *

def comment():
    out = ""
    for i in getSelection().split("\n"):
        if i[0] == "#":
            out += i[1:] + "\n"
        else:
            out += "#" + i + "\n"
    placeText(out)

def addTab():
    out = ""
    for i in getSelection().split("\n"):
        out += "    " + i + "\n"
    placeText(out)

def removeTab():
    out = ""
    for i in getSelection().split("\n"):
        if i[0:4] == "    ":
            out += i[4:] + "\n"
    placeText(out)