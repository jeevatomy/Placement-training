'''
Given an input of string in combinations of characters '{' and '}', which are parenthesis, you have to find if the input is balanced or not. The input is balanced if all the opening curly braces are closed. You can't close a curly brace before it is opened.

Input Format

Read a string from the console

Constraints

NA

Output Format

If the input is balanced print "Matching" on the console, else print "Not Matching"


'''


s=input()
stack=[]
for char in s:
    if char=="{":
        stack.append(char)
    elif char=="}" and len(stack)!=0:
        stack.pop()
if len(stack)==0:
    print("Matching")
else:
    print("Not Matching")
