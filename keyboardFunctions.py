import keyboard
from time import sleep
from clibboard import *

def pressed(keyCombination):
    return keyboard.is_pressed(keyCombination)

def getSelection():
    prevCopy = getClipboard()
    keyboard.press_and_release('ctrl+c')
    sleep(0.1)
    returnValue = getClipboard()
    writeFile(returnValue)
    setClipboard(prevCopy)
    return returnValue

def placeText(text):
    prevCopy = getClipboard()
    sleep(0.1)
    setClipboard(text[:-1])
    sleep(0.1)
    keyboard.press_and_release('ctrl+v')
    sleep(0.1)
    setClipboard(prevCopy)

def writeFile(Text):
    myfile = open("previousText.txt", 'w')
    Text = Text.replace("\n", "")
    myfile.write(Text)
    myfile.close()