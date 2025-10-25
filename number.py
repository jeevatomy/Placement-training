def numtobin(m):
    l=[]
    while m>0:
        r=m%2
        l.append(r)
        m=m//2
    return l[::-1]

def bintonum(b):
    n=0
    for i in range(len(b)):
        n+=(2**i)*b[i]
    print(n)
n=int(input())
b=numtobin(n)
bintonum(b)
        
    
        
