from keyboardFunctions import *
from functions import *

if __name__ == "__main__":

    while True:
        if altPressed('c'):
            comment()
        if altPressed('right'):
            addTab()
        if altPressed('left'):
            removeTab()
        if altPressed('q'):
            break