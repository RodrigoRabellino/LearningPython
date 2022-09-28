pages = [
    "Page 0) \n Once upon a time... \nWhat do you want to do? \nOp.1... \nOp.2... \nOp.3... ",
    "Page 1) \n Once upon a time... \nWhat do you want to do? \nOp.1... \nOp.2... \nOp.3... ",
    "Page 2) \n Once upon a time... \nWhat do you want to do? \nOp.1... \nOp.2... \nOp.3... ",
    "Page 3) \n Once upon a time... \nWhat do you want to do? \nOp.1... \nOp.2... \nOp.3... ",
    "Page 4) \n Once upon a time... \nWhat do you want to do? \nOp.1... \nOp.2... \nOp.3... ",
]

def showPage(pageNum):
    print(pages[pageNum])
    resp= input()
    showPage(int(resp))
    
showPage(0)