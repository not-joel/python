# append

mylist = []
my_string = 'hello'
for letter in my_string:
    mylist.append(letter)
print(mylist)

# list comprehension
# flattened for loop
mylist = [letter for letter in my_string]
print(mylist)

num_list = [num**2 for num in range(0, 10)]
print(num_list)

# list comprehension with 'if' statement
list1 = [num**2 for num in range(0, 11) if num%2==0]
print(list1)

celsius = [0, 10, 20, 34.5]

fahrenheit = [((9/5) * temp + 32) for temp in celsius]
print(fahrenheit) 

# if else
results = [x if x%2 == 0 else 'ODD' for x in range(0, 11)]
print(results)


# nested loops
list2 = []

for x in [2,4,6]:
    for y in [1, 10, 100]:
        list2.append(x*y)
print(list2)

# now using list comprehension
list3 = [x*y for x in [2,4,6] for y in [1,10,100]]
print(list3)