#print the table of odd numbers 1 to 10
for i in range (1,11,2):
    print ("Table",i)
    for j in range (1,11):
        print (i,"*",j,"=",i*j)
    print()