# set operations (union , intersection , differnce , symmetric differnce)


# Intersection of Two Sets

def intersection_of_sets(set1, set2):
    return set1.intersection(set2)      # (or) set1 & set2

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
result = intersection_of_sets(set1, set2)
print(result)  # Output: {4, 5}

# union of two sets

def union_of_sets(set1, set2):
    return set1.union(set2)            #(or) set1 | set2

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
result = union_of_sets(set1, set2)
print(result)  # Output: {1,2,3,4,5,6,7,8}


#differnce of two sets

def difference_of_sets(set1, set2):
    return set1.difference(set2)      # (or) set1 - set2

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
result = difference_of_sets(set1, set2)
print(result)  # Output: {1, 2, 3}


#symmetric differnce of two sets

def sym_difference_of_sets(set1, set2):
    return set1.symmetric_difference(set2)      # (or) set1 ^ set2

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
result = sym_difference_of_sets(set1, set2)
print(result)  # Output: {1, 2, 3, 6, 7, 8}


# replacing an elemnt


num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]
n = int(input())
new_list = []

for tuple_a in num_list:
    update_tuple = tuple_a[:-1] + (n,)
    new_list.append(update_tuple)

print(new_list)


#Remove Duplicates from a List using a Set

def remove_duplicates_with_set(input_list):
    unique_set = set()
    result_list = []
    for item in input_list:
        if item not in unique_set:
            result_list.append(item)
            unique_set.add(item)
    return result_list

my_list = [1, 2, 2, 3, 3, 4, 5, 5]
result = remove_duplicates_with_set(my_list)
print(result)  # Output: [1, 2, 3, 4, 5]


#another way

my_list = [1, 2, 2, 3, 3, 4, 5, 5]
print(list(set(my_list))) #output:[1, 2, 3, 4, 5]


