
def reverse(x):

    x = x[::-1]
    

    
    for i in range(len(x)):
        if type(x[i]) == list:
            x[i] = reverse(x[i])
            
    
    

    else:
        return x
x = eval(input())
print(reverse(x))