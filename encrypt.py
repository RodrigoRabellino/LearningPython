numCrypt = 5
def crypt(text):
    finalText = ""
    for word in text: 
        finalText += chr(ord(word) - numCrypt)  
    return finalText

def decrypt(text):
    finalText = ""
    for word in text: 
        finalText += chr(ord(word) + numCrypt)  
    return finalText
    
    
def cryptTxtFile(fileName): 
    text = open(fileName, "r").read()
    cryptFile = open("processed/crypt.txt", "w")
    cryptFile.write(crypt(text))
    cryptFile.close()
    print("crypt finished")
    
def decryptTxtFile(fileName): # processed/crypt.txt
    text = open(fileName, "r").read()
    cryptFile = open("processed/decrypt.txt", "w")
    cryptFile.write(decrypt(text))
    cryptFile.close()
    print("decrypt finished")
    
result = input("select 'E' for crypt file, or 'D' for decrypt: ")
pathFile = input("set file path: ")

if (pathFile != ""):
    if (result.upper() == "E"):
        cryptTxtFile(pathFile)
    if (result.upper() == "D"):
        decryptTxtFile(pathFile)
else: 
    print("path cannot be empty")