#Tuples #collection of ordered elements that cannot be modified but also allow duplicates

my_tuple = (1, 2, 3 , 4, 5)

print(my_tuple)
print(my_tuple[0])
print(my_tuple[2])
print(my_tuple[-1]) #a negative will always give the last item on lists and tuples

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

conc_tuple = tuple1 + tuple2 #adding tuples together
print(conc_tuple)

rep_tuple = tuple1 * 3 #repeatition
print(rep_tuple)
