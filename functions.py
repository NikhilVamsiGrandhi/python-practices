#count of lower_case and upper_case

def count_of_lowercase_and_uppercase_letters(arg_1):
    count_of_uppercase=0
    count_of_lowercase=0
    for i in arg_1:
        if i==i.upper():
            count_of_uppercase+=1
        else:
            count_of_lowercase+=1

    print(count_of_uppercase)
    print(count_of_lowercase)


#longest_increasing_subsequence
def longest_increasing_subsequence(sequence):
    list_num = []
    num = sequence[0]
    list_num.append(num)

    for i in range(len(sequence)):
        for j in (sequence[i:]):
            if num < j:
                list_num.append(j)
                num = j
                break
    return list_num


sequence = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_increasing_subsequence(sequence))


# smallest sum of n elements

num=sorted(list(map(int,input().split(',')))) # 9,8,7,4,5,6,1,2,3
index=int(input())                            # 4
sum=0
for i in range(index):
    sum+=num[i]
print(sum)                                    # output:- 10
