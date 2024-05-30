x = 10

# while - else
while x < 5:
    print(x)
    x += 1
else:
    print('X is not less than 5')
    

# break, continue, pass
# break: Breaks out of the current closest enclosing loop
# continue: Goes to the top of the closest enclosing loop
# pass: Does nothing at all

# PASS
x = [1, 2, 3]

for item in x:
    # comment
    pass

print('end of my script')

# CONTINUE
mystring = 'Joel'

for letter in mystring:
    if letter == 'e':
        continue
    print(letter)
    
# BREAK
for letter in mystring:
    if letter == 'e':
        break
    print(letter)

n = 0

while n < 5:
    if n == 2:
        break
    print(n)
    n += 1