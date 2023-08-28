#if,elif,else
'''
age=int(input())
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are exactly 18.")
else:
    print("You are an adult.")
'''

#greatest among the three
'''
a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print((b))
else:
    print(c)
'''

#amstrong number

a=input()
num=0
for i in a:
    b=int(i)**len(a)
    num+=b
if num==int(a):
    print("amstrong number")
else:
    print("no")