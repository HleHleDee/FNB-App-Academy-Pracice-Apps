
fruits = ["apple", "banana", "cherry"] #python lists are zero index meaning the apple is 0, banana 1,cherry 2
print(fruits[0]) 

fruits[1] = "blueberry" #replacing index 1 which is banana by blueberry

print(fruits)

fruits = ["apple", "banana", "cherry"]

fruits.append("kiwi") #adding an item on list
print(fruits)

fruits.insert(1, "orange") #adding a value in a specific position to the list
print(fruits)

fruits.remove("kiwi") #removing items
print(fruits)

fruits.sort() #ascending order
print(fruits)

fruits.sort(reverse=True) #descending order
print(fruits)