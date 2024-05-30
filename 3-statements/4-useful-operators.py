# range

# range(stop)
# range(start, stop, step)
for num in range(1, 10, 2):
    print(num)
    
# range ---> GENERATOR
print(range(1, 10, 2))

print(list(range(1, 10, 2)))

# enumerate

index_count = 0
word = 'abcde'
for letter in word:
    print(f'At index {index_count} the letter is {letter}')
    index_count += 1
    
for (index, letter) in enumerate(word):
    print(index)
    print(letter)
    
# ZIP

# zips the data at particular location in memory
# if list size uneven - takes only till matching index
mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]
print(zip(mylist1, mylist2, mylist3))

for item, letter, num in zip(mylist1, mylist2, mylist3):
    print(item)
    print(letter)
    print(num)
print(list(zip(mylist1, mylist2, mylist3)))


# in - keyword
print(2 in [1, 2, 3])
print('x' in ['x', 'y', 'z'])
print('o' in 'a word')
print('myKey' in {'myKey': 123})
d = {'myKey': 123}
print(123 in d.values())


# min & max
print(min(mylist1))
print(max(mylist1))


# Random

from random import shuffle

newlist = [1,2,3,4,5,6,7,8,9,10]
shuffle(newlist) # not assignable
print(newlist)

from random import randint
my_num = randint(0, 100)
print(my_num)


# USER INPUT
result = int(input('Enter a number: '))
print('RESULT --> ', result)
print(type(result))