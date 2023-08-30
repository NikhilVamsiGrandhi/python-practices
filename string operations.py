#strings length
text = "Hello, World!"
length = len(text)
uppercase = text.upper()
lowercase = text.lower()
print(uppercase)
print(length)


#string operations

str = "Hello"
str1 = " world"
print(str*3) # prints HelloHelloHello
print(str+str1)# prints Hello world
print(str[4]) # prints o
print(str[2:4]); # prints ll
print('w' in str) # prints false as w is not present in str
print('wo' not in str1) # prints false as wo is present in str1.'''

#diamond

n=int(input("Enter a number: "))

for i in range(1,n+1):
    left_spaces=" "*(n-i)
    middle_s=" "*((i-1)*2)
    print(left_spaces+"/"+middle_s+"\\")
for i in range(1,n+1):
    left_spaces=" "*(i-1)
    middle_s=" "*((n*2)-(i*2))
    print(left_spaces+"\\"+middle_s+"/")'''


#String Manipulation with reversed and with out it

#1

sentence = "Python is an amazing language"
sentence=sentence.split()
reversed_sentence = ' '.join(sentence[::-1])
print(reversed_sentence)

#2
sentence = "Python is an amazing language"
# Reverse the sentence
reversed_sentence = ' '.join(reversed(sentence.split()))
print(reversed_sentence)

#re module (uses)

import re

text = "Email me at alice@example.com or bob@example.net"
emails = re.findall(r'\S+@\S+', text)
print(emails)



