# st = 'Print only the words that start with s in this sentence'

# words = st.split()
# for word in words:
#     if word[0] == 's':
#         print(word)
        
# # 2
# for num in range(0, 11, 2):
#     print(num)

# alternate
# print(list(range(0, 11, 2)))
        
# # 3
# divisibles = [num for num in range(1,51) if num%3==0]
# print(divisibles)

# # 4
# st = 'Print every word in this sentence that has an even number of letters'

# words = st.split()
# for word in words:
#     if (len(word) % 2 == 0):
#         print('even')


# # 5
# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print('FizzBuzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else:
#         print(num)


# 6
st = 'Create a list of the first letters of every word in this string'
result = [word[0] for word in st.split()]
print(result)