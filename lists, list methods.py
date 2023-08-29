
#Rotate List Elements

def rotate(lsit,k):
    n=len(lsit)
    a=k%n
    print(a)
    return (lsit[-a:]+lsit[:-a])

lsit_a=list(map(int,input().split()))
print(rotate(lsit_a,1))



#Find the Intersection of Two Lists


def intersection(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = intersection(list1, list2)
print(result)  # Output: [3, 4, 5]



#longest subsequence

def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n
    print(lis)

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                print(lis[i])

    return max(lis)

sequence = [10, 22, 9, 33, 21, 50, 41, 60, 80]
result = longest_increasing_subsequence(sequence)


#first and last element of the list

n=int(input())
x=[]
for i in range(n):
    i=int(input())
    x+=[i]
print(x[:2]+x[-2:])


# average of the given numbers

list_a = input().split()
leng = len(list_a)
sum_a = 0
for i in list_a:
    sum_a += int(i)

print(round((sum_a / leng), 2))
