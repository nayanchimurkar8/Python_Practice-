# Accept the name and check if its Palindrome.
name = input("Enter Name: ")
if name[::-1] == name:
    print(name,"is a Palindrome")
else:
    print(name,"is not a Palindrome")
    