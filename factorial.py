'''
Write a program to find the factorial of a number using recursion.

Input Format

Read a number n from the console

Constraints

NA

Output Format

Print the factorial of the number n



'''


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input())
fact=factorial(n)
print(fact)
