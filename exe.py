values = [12, 45, 2, 67, 34, 89]
values.sort()
print(values)

colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
item_to_count = 'blue'
count = colors.count(item_to_count)
print(f"The item '{item_to_count}' appears {count} times in the list")

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

data =[]
if not data:
    print("the list is empty")
else:
  print("the list is not empty")    

nums = [1, 2, 3, 4, 5, 6]
squares_of_even = [x**2 for x in nums if x % 2 == 0]
print(squares_of_even)

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

combined = [x for x in zip(list1, list2) for x in x]
print(combined)
