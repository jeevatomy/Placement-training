n=int(input())
arr=list(map(int,input().split()))
q=int(input())
l=[]
for i in range(q):
    m=int(input())
    l.append(m)
for num in l:
    if num<min(arr):
        print("Smaller: 0, Greater:",n)
    elif num>max(arr):
        print("Smaller: ",n,","," Greater: 0", sep="")
    else:
        s=0
        g=0
        for nu in arr:
            if nu<num:
                s+=1
            elif nu>num:
                g+=1
        print("Smaller: ",s,","," Greater: ",g, sep="")
            
        
        
