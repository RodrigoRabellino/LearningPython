from datetime import datetime
contractFile = open("contract.txt" , "r")
result = ""
data = {
    "[COMPANY_NAME]": "", 
    "[CURRENT_DATE]": datetime.today().strftime("%d/%m/%Y"), 
    "[EMPLOYEE_NAME]": "", 
    "[CITY]": "", 
    "[COUNTRY]": "", 
    "[PRICE]": "", 
}

def normalizeText(text): 
    return text.replace("[", "").replace("]", "").replace("_", " ").lower()

def setData():
    for dataKey in data.keys(): 
        if data[dataKey] == "":
            print("set " + normalizeText(dataKey) + ":")
            newValue = input()
            data[dataKey] = newValue

setData()


def replaceText(text, completeData): 
    for dataKey in completeData.keys():
        text = text.replace(dataKey, completeData[dataKey])
    return text

# save content file in a new variable and update data
for row in contractFile: 
    result += replaceText(row, data)
    
    
    
#save new file whit a new data     
with open("processed/contract_processed.txt", "w") as textFile:
    textFile.write(result)
    
