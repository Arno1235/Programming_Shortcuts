import win32clipboard
from time import sleep

def getClipboard():
    win32clipboard.OpenClipboard()
    try:
        returnValue = win32clipboard.GetClipboardData()
    except:
        returnValue = None
    win32clipboard.CloseClipboard()
    return returnValue

def setClipboard(Text):
    win32clipboard.OpenClipboard()
    try:
        win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, Text)
    except:
        None
    win32clipboard.CloseClipboard()