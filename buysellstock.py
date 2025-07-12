'''
Write a program that takes an array that denotes the daily closing prices of a stock to determine the maximum profit by buying and selling one share of the stock.

Input Format

9
310 315 275 260 270 290 230 255 250

Constraints

NA

Output Format

30
'''


n=int(input())
arr=list(map(int,input().split()))
minprice=arr[0]
maxprofit=0

for price in arr:
    if price<minprice:
        minprice=price
    profit=price-minprice
    maxprofit=max(maxprofit,profit)
print(maxprofit)
