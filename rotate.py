n,k=map(int,input().split())
k=k%n

arr=list(map(int,input().split()))
arr1=arr[n-k:]+arr[:n-k]
print(" ".join(map(str,arr1)))
