def ispal(m):
    return m==m[::-1]
s=input()
found=0 
if len(s)==0:
    print("NO")
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        a,b,c=s[:i],s[i:j],s[j:]
        if ispal(a) and ispal(b) and ispal(c):
            found=1
            break
    if found:
        break

if found==1:
    print("YES")
else:
    print("NO")
            
            
        
    
    
