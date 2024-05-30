# iterate strings
# iterate elements in list
# iterate keys in dictionary

# for _ in 'Hello World':
#     print('Cool')

# my_list = [1,2,3,4,5,6,7,8,9,10]
# list_sum = 0

# for num in my_list:
#     list_sum += num

# print(list_sum)

# tuple unpacking

# new_list = [(1,2), (3,4), (5,6), (7,8)]

# for (a, b) in new_list:
#     print('a:', a)
#     print('b:', b)
    
# new_list = [(1,2,3), (4,5,6), (7,8,9)]

# for (a, b, c) in new_list:
#     print('a:', a)
#     print('b:', b)
    
d = {
    'k1': 1,
    "k2": 2,
    "k3": 3
}


for item in d.items():
    print(d)
    
for item in d:
    print(d[item])

# alternate
for (key, value) in d.items():
    print(value)

for value in d.values():
    print(value)