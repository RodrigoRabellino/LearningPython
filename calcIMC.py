# imc = peso / (alturax altura)
# < 19: delgadez
# 20 - 25: normal
# 26 - 30: alto
# > 30 : sobrepeso


userData ={"weight": 0, "height": 0}

def calcImc(data):
    calc = data["weight"] / ((data["height"] / 100) ** 2)
    print("your imc: " + str(calc))
    if(calc <= 19):
       return print("thin")
    if(calc >= 20 and calc <= 25):
       return print("normal")
    if(calc >= 26 and calc <= 30):
       return print("hight")
    return print("overweight")
    
    
def setData(): 
    for key in userData.keys():
        newValue = float(input("set " + key + ": "))
        userData[key] = newValue
    calcImc(userData)
        
setData()