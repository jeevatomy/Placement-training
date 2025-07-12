'''

Given a sorted (in ascending order) integer array nums of n elements and a target value, find if there exists any pair of elements (nums[i], nums[j], i!=j) such that their sum is equal to target.

Solve this problem using the Two-pointers concept. The complexity should not be O(N-square) or more

Input Format

5
-3 -1 0 1 2
-2

Constraints

1 < nums.length <100

Output Format

Yes'''

def t(arr,x):
    left=0
    right=len(arr)-1

    while left<right:
        if arr[left]+arr[right]<x:
            left+=1
        elif arr[left]+arr[right]>x:
            right-=1
        elif arr[left]+arr[right]==x:
            return "".join("Yes")
    return "".join("No")

n=int(input())
arr=list(map(int,input().split()))
x=int(input())
s=t(arr,x)
print(s)
