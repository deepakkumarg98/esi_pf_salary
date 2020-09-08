'''
help no : 1

def test(a,b):
    a=set(a)
    b=set(b)
    c=list(b&a)

    if c:
        print("Union : ",c[0],c[1])
    else:
        print(c)
        
a=[10,12,14,16]
b=[1,2]
test(a,b)

'''
    
import pandas as pd

with open('test.txt', 'w') as file:
    pd.read_excel('data.xlsx').to_string(file, index=False)
