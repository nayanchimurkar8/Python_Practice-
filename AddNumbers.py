#add two number at third position on the list
numbers =[10,20,30,40,50]
a = int(input("Enter no: "))
b = int(input("enter 2nd no: "))
sum = a + b
numbers.insert(2,sum)
print("Added two Numbers list: ",numbers)

