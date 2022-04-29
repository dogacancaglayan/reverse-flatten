

def flatten(x):
    control = True
    for i in x:
        if type(i) == list:
            control = False
        
    if control == True:
        return x
    
    outputList = []
    
    
    for i in x:
        
        if type(i) == list:
            for a in i:
                outputList.append(a)
        else:
            outputList.append(i)

    return flatten(outputList)

x = eval(input())
print(flatten(x))
    
    
    
        