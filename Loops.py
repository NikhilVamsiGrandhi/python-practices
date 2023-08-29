#while and for

#sum of non prime numbers

n = int(input())
count = 0

for i in range(n):
    m = int(input())
    for j in range(2, m):
        if m % j == 0:
            count = count + m
            break
        else:
            pass

print(count)



#right triangle

n=int(input())
count=""
a="1"
for i in range(1,n+1):
    count=a*(i)
    spaces=" "*(n-i)
    power=int(count)**2
    print(spaces+str(power))


