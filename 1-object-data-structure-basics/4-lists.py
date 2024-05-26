# LISTS

my_list = ['one', 'two', 'three']
print(my_list[::-1]) # reverse
my_list[2] = 'six'
print(my_list)
another_list = ['four', 'five']
print(my_list + another_list)

new_list = my_list + another_list
new_list.append('seven') # adds element at the END
print(new_list)

# .pop() default position -1
new_list.pop()
print(new_list)

popped_item = new_list.pop()
print(popped_item)

new_list.pop(0)
print(new_list)

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]

# .sort() does not return anything 
# So cannot assign to variable
new_list.sort() 
print(new_list)
num_list.sort()
num_list.reverse()
print(num_list)

nested_list = [1, 2, [3, 4]]
print(nested_list[2][1])