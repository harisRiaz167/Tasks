# find sum of three numbers
addNumbers = lambda x,y,z : x+y+z

user_input = int(input("Enter first number: "))
user_input2 = int(input("Enter second number: "))
user_input3 = int(input("Enter third number: "))
print('Your final ans: ', addNumbers(user_input,user_input2,user_input3))

# Swap alphabets
swapString = lambda string : string.swapcase()

userString = input("Enter your string: ")
print('swap string is: ', swapString(userString))

# Filter odd numbers from the list
newList = []
n = int(input("Enter total elements in list: "))
for i in range(n):
    user_input = int(input("Enter number for add in list: "))
    newList.append(user_input)
print("intial list: ",newList)

evenNumbers = list(filter(lambda li : (li % 2 == 0),newList))
print('Even Number list: ', evenNumbers)

