from keyboardFunctions import *
from functions import *

if __name__ == "__main__":
    while True:
        if pressed('ctrl+i'):
            comment()
            break
        if pressed('ctrl+up'):
            addTab()
            break
        if pressed('ctrl+down'):
            removeTab()
            break