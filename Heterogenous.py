#Create a heterogenous list of numbers and names.split the list from highest number.
my_list = ["Nayan",1,"Harsh",2,"Parth",3]
print("Original List:", my_list)

numbers = [x for x in my_list if isinstance(x, (int, float))]
highest = max(numbers)
print("Highest Number:", highest)

index = my_list.index(highest)
list1 = my_list[index]
list2 = my_list[index]
print("First list", list1)
print("Highest no list:", list2)
