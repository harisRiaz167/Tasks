# Array Concatenation
import array as arr

arr1 = arr.array('i',[3,5,6,7,8])
arr2 = arr.array('i',[4,6,8,9,10])
arr3 = arr.array('i')
arr3 = arr1+arr2
print(arr3)


# Changing list into arrays
import numpy as np

newList = []
list = int(input("Enter total elements in list: "))
for user_input in range(list):
      user_input = int(input("Enter number for add in list: "))
      newList.append(user_input)
print("original list: ",newList)
print('array of list: ', np.asarray(newList))



