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
    
