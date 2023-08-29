# Find the Second Largest Element in a Tuple

def second_largest_element(tuple):
    sorted_tup = sorted(tuple, reverse=True)
    return sorted_tup[1]

my_tuple = (10, 22, 9, 33, 21, 50, 41, 60, 80)
result = second_largest_element(my_tuple)
print(result)  # Output: 60


#Merge Two Tuples Without Duplicates

def without_duplicates(tuple1,tuple2):
    merged_tuple=tuple(set(tuple1) | set(tuple2))
    return merged_tuple

tuple_1=(1,2,3,4,5,6)
tuple_2=(4,5,6,7,8,9)
new_tuple=without_duplicates(tuple_1,tuple_2)
print((new_tuple))


#Count the Occurrences of Each Element in a Tuple

def count_occurrences(tup):
    element_count = {}
    for item in tup:
        if item in element_count:
            element_count[item] += 1
        else:
            element_count[item]=1
    return element_count

my_tuple = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
result = count_occurrences(my_tuple)
print(result)  # Output: {1: 1, 2: 2, 3: 3, 4: 4}