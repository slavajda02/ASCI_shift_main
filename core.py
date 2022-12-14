import numpy as np
import tkinter

def encrypt(string, key):
    key = keyConvert(key)
    if key == "WRONG_FORMAT":
        tkinter.messagebox.showerror("Error", "From key format")
        return "", key
    
    asciiL = []
    # convert input string to ascii list
    for x in string:
        asciiL.append(ord(x))

    # shift ascii value of asciiVar "asciiL"
    i = 0
    for x in range(len(asciiL)):
        if i == len(asciiL) or i == len(key):
            i = 0
        asciiL[x] += key[i]
        if asciiL[x] > 126:
            asciiL[x] = asciiL[x] - 126 + 31
        i += 1

    # Converting ascii to string
    string = []
    for x in asciiL:
        string.append(chr(x))
    string = "".join(string)
    return string

def decrypt(string, key):
    key = keyConvert(key)
    asciiL = []
    # convert input string to ascii list
    for x in string:
        asciiL.append(ord(x))
        
    # shift back ascii value of asciiVar "asciiL"
    i = 0
    for x in range(len(asciiL)):
        if i == len(asciiL) or i == len(key):
            i = 0
        asciiL[x] -= key[i]
        if asciiL[x] < 31:
            asciiL[x] = asciiL[x] + 126 - 31
        i += 1
        
    # Converting ascii to string
    string = []
    for x in asciiL:
        string.append(chr(x))
    string = "".join(string)
    return string

def keyGenerator():
    key = []
    for i in range(8):
        key.append(format(np.random.randint(0,255), 'x'))
    return "".join(key)    

def keyConvert(key):
    try:
        convKey = [key[i:i+2] for i in range(0, len(key), 2)]
        for x in range(len(convKey)):
            convKey[x] = int(convKey[x], 16)
    except ValueError:
        return "WRONG_FORMAT"
    
    return convKey
