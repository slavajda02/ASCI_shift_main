def encrypt(string, key):
    key = keyConvert(key)
    asciiL = list(string.encode('ascii'))
    i = 0
    for x in range(len(asciiL)):
        if i ==len(asciiL):
            i = 0
        asciiL[x] += key[i]
        string = asciiL.join(chr(asciiL))    
        print(string)
    
def kecrypt(string, key):
    next
    
def keyGenerator():
    next
    
    
def keyConvert(key):
    convKey = [key[i:i+2] for i in range(0, len(key), 2)]
    for x in range(len(convKey)):
        convKey[x] = int(convKey[x], 16)
    return convKey