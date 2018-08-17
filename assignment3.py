
from collections import deque
1.
b=[]
r=int(input())
for i in range(r):
    a=input("enter string")
    b.append(a)
print(b)

2.
c=["google","apple","facebook","microsoft","tesla"]
t=b+c
print(t)

3.
l=['am','am','hie','hello']
b=input("enter string whose no to be counted")
n=l.count(b)
print(n)


4.
a=int(input("enter no"))
b=[]
for i in range(a):
    c=input("enter no")
    b.append(c)
print(b)
b.sort()
print(b)


5.
A=[12,5,76,23,68]
B=[3,8,32,67,44]
n=A+B
n.sort()
print(n)

6.
stack=["aa","bb","cc","dd"]
stack.append("kaur")
stack.append("amrit")
print(stack.pop())
print(stack)

q1=deque(["am","tt","ee","jj"])
q1.append("amrit")
print(q1.popleft())


7.
c=0;
b=0;
a=[12,4,7,9,5]
for i in a:
    if(i%2==0):
        c=c+1
    else:
        b=b+1
print("even no =",c)
print("odd no =",b)


8.
# Print tuple in reverse order
a=('apple','banana','mango','orange','cherry')
print(a[ ::-1])


9.
# Find largest and smallest element in a tuple
print("largest element",max(a))
print("Smallest element",min(a));


10.
# Convert a string into Uppercase
a=input("enter string")
print(a.upper())


11.
# Check if string contains all numeric characters
a=input("enter string")
print(a.isnumeric())


12.
# Replace the word "World" with your name in string "Hello World"
c="Hello World"
d=c.replace("World","Amrit")
print(d)

