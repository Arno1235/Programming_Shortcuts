import keyboard

def pressed(keyCombination):
    return keyboard.is_pressed(keyCombination)

def getSelection():
    keyboard.press('ctrl+c')

def placeText(text):
    keyboard.write(text)