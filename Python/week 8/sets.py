#Sets 
# #un ordered collection of unique elements-don,t allow duplicates values-can add and remnove-useful when you want to perform operations like union into section and difference between collection of elements
'''
my_set = {1, 2, 3, 4, 5}

print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)

'''

set1 = {1, 2, 3}
set2 = {3, 4, 5}

#union-adds both sets together and removes any duplicate data
union_set = set1.union(set2)
print(union_set)

#Intersection-finds common element between two sets
inter_set = set1.intersection(set2)
print(inter_set)

#Difference-finds elements that are present in one but not in the other
diff_set = set1.difference(set2)
print(diff_set)