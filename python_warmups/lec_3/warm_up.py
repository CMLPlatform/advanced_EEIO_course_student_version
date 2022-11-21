import numpy as np

### Question 1.a
result = 3 / 5
print(f"Result: {result} with type {type(result)}")

result = 3 * 5
print(f"Result: {result} with type {type(result)}")

### Question 1.b
result = 4.5 * 5
print(f"Result: {result} with type {type(result)}")

### Question 1.c
value_list = [3, 4, 5, 7.3]
result = sum(value_list)
print(f"Result: {result} ")

### Question 1.d
# List indexes in python start from 0, so the second item is at index 1.
second_item = value_list[1]
print(f"Second item 4 is equal to second item: {second_item == 4}")

### Question 2.a
integer_list = [1, 2, 3, 4, 5, 5, 7, 34567, 7754]
array_one = np.array(integer_list)
print(array_one)

### Question 2.b
print(f"{array_one + 3}")

### Question 2.b
print(f"{array_one / 5}")

### Question 2.c
# You can create an array from a list of lists
array_two = np.array([
    [2, 6.7, 8],
    [4, 3.14, 24]
])
print(f"Array two looks like:\n{array_two}\nand its shape is {array_two.shape}")

### Question 2.d
# np.sum(array_two) or array_two.sum(): both return the sum of all values in the array.
print(f"Sum of array: {array_two.sum()}")

### Question 2.e
# We can sum over an axis of the array, axis 0 are the rows, axis 1 are the columns.
# To find the sum of the rows, we collapse axis 1 (the columns)
print(f"Sum rows: {array_two.sum(axis=1)}")

### Question 2.f
print(f"Sum rows:\n{array_two.sum(axis=1, keepdims=True)}")
