# open file 
contractFile = open("contract.txt" , "r")
result = ""
data = {
    "[COMPANY_NAME]": "", 
    "[CURRENT_DATE]": "", 
    "[EMPLOYEE_NAME]": "", 
    "[CITY]": "", 
    "[COUNTRY]": "", 
    "[PRICE]": "", 
}

print("Company Name: ")
cName = input()
data["[COMPANY_NAME]"] = cName;


def replaceText(text, completeData): 
    for dataKey in completeData.keys():
        text = text.replace(dataKey, completeData[dataKey])
    return text

# save content file in a new variable and update data
for row in contractFile: 
    result += replaceText(row, data)
    
    
    
#save new file whit a new data     
with open("contract_processed.txt", "w") as textFile:
    textFile.write(result)
    
