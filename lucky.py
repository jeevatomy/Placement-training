n1=int(input())
n2=int(input())
count=0
for i in range(n1,n2+1):
    l=set()
    while i>0:
        r=i%10
        if r in l:
            break
        else:
            l.add(r)
        i=i//10
    else:
        count+=1
        
 
print(count)
