n=int(input())
arr=list(map(int,input().split()))
arr1=list(map(int,input().split()))
arr.sort()
arr1.sort(reverse=True)
s=0
for i in range(n):
    s+=arr[i]*arr1[i]
print(s)
    
