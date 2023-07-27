# Create a tuple with five elements and convert it into a list.
# x=(1,2,3,4,5)
# y=list(x)
# print(y)
# x=(1,2,3,4,5)
# print(list(x))
# Create a tuple with ten elements and print the last three elements using slicing.
# x=(1,2,3,4,5,6,7,8,9,10)
# print(x[7:10])
# x=(1,2,3,4,5,6,7,8,9,0)
# print(x[7:10])

# Create a tuple with five elements and unpack it into five variables.
# x=(1,2,3,4,5)
# a,b,c,d,e=x
# print(a,b,c,d,e)
# x=(1,2,3,4,5)
# a,b,c,d,e=x
# print(a,b,c,d,e)

# Create two tuples with three elements each and concatenate them into a single tuple.
# x=(1,2,3)
# y=(4,5,6)
# z=x+y
# print(z)
# x=(1,2,3)
# y=(4,5,6)
# z=x+y
# print(z)

# Create a tuple with five elements and find the index of an element in it.
# x=(1,2,3,4,5)
# y=x.index(5)
# print(y)

# x=(1,2,3,4,5)
# b=x.index(4)
# print(b)

# Create a tuple with five elements and check if a specific element is present in it.
# python
# Copy code
# my_tuple = (1, 2, 3, 4, 5)
# if 3 in my_tuple:
#     print("Element 3 is present in the tuple")
# else:
#     print("Element 3 is not present in the tuple")
# Output:

# python
# Copy code
# Element 3 is present in the tuple
# x=(1,2,3,4,5)
# if 3 in x:
#     print("yes")
# else:
#     print("no")


# Create a tuple with five elements and convert it into a dictionary where the elements are the keys and their indices are the values.
# x=('a','b','c','d','e')
# dicto={}
# for i in range(len(x)):
#     dicto[x[i]]=i
# print(dicto)
# x=(1,2,3,4,5)
# dict={}
# for i in range(len(x)):
#     dict[x[i]]=i
# print(dict)

# Create a tuple with three elements and compare it with another tuple with the same elements but in a different order.
# python
# Copy code
# tuple1 = (3, 7, 5)
# tuple2 = (5, 3, 7)

# if tuple1 == tuple2:
#     print("The two tuples are equal.")
# else:
#     print("The two tuples are not equal.")
# Output: The two tuples are not equal.

# Here's an example of creating a tuple with five elements and removing an element from it:
# x=(1,2,3,4,5)
# y=list(x)
# y.remove(5)
# x=tuple(y)
# print(x)

x=(1,2,3,4,5)
b=list(x)
b.remove(4)
print(b)

# x=(1,2,3,4,5,6,7,8,9,10)
# print(x[7:11])
# b=list(x)
# b.remove()
# print(b)
