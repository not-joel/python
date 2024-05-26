# Tuples

# Tuples are similar to list
# Difference -> Tuples are immutable (cannot be re-assigned)
# Tuples use paranthesis --> (1, 2, 3)

t = (1, 2, 3)
my_list = [1, 2, 3]

print(type(t))
print(type(my_list))

t = ('one', 2)
print(t[0])

t = ('a', 'b', 'a')
print(t.count('a'))
print(t.index('a')) # gives the 1st occurence