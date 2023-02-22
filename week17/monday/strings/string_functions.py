print("Spaghetti".index('h')) # => 4
print("Spaghetti".index('t')) # => 6, first t

# value not in string will error

# count => how many times a substring apperas in the primary string

print("Spaghetti".count("h"))    # => 1
print("Spaghetti".count("t"))    # => 2
print("Spaghetti".count("s"))    # => 0
print('''We choose to go to the moon in this decade and do the other things,
not because they are easy, but because they are hard, because that goal will
serve to organize and measure the best of our energies and skills, because that
challenge is one that we are willing to accept, one we are unwilling to
postpone, and one which we intend to win, and the others, too.
'''.count('the '))

# concatenation

print('gold' + 'fish')
print('s'*7)
print('$1' + ',000'*3)

# formatting
first_name = 'Billy'
last_name = 'Bob'

print('Your name is {0} {1}'.format(first_name, last_name)) 
print(f'Your name is {first_name} {last_name}')

# join 
s = "--".join(["it", "is", "kind"]) 
print(s)