# ASSESSMENT - 1

# operators
x = (5 ** 2 * 4) / 2 + (101 - 50.75)
print(x)

y = 4 ** 2
# z = y ** (1/2)
z = y ** .5

# string
s = 'hello'
print(s[1])
print(s[::-1])

str_length = len(s)
print(s[str_length - 1])
print(s[-1])

# list
# my_list = []
# new_list = [0, 0]
# my_list = my_list + new_list
# # print(my_list)
# my_list.insert(2, 0)
# print('LIST', my_list)

list1 = [0]*3
print('list1', list1)
list2 = [0, 0, 0]
print('list2', list2)

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

list4 = [5,3,4,6,1]
l = sorted(list4)
print('--->', l)
list4.sort()
print('list4', list4)

# dictionary

d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print('--->', d['k1']['k2'])

d1 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d1['k1'][0]['nest_key'][1][0])

d2 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d2['k1'][2]['k2'][1]['tough'][2][0])

# Tuple

t = (1, 2, 'three')
print(t)

# Set

list5 = [1,2,2,33,4,4,11,22,3,3,2]
my_set = set(list5)
print(my_set)

# Boolean

print(3.0 == 3)
print(4 ** .5 != 2)

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
print(l_one[2][0] >= l_two[2]['k1'])