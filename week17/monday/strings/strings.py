# writing valid strings

print("Hey Programmers")

print('Hey Programmers!!!')

print("It's a nice day.")

print('''My instructions are very long so to make them
more readable in the code I am putting them on
more than one line. I can even include "quotes"
of any kind because they won't get confused with
the end of the string!''')

# Calculating length with len()
print(len('Spaghetti')) # => 9

# indexing a string

print('Spaghetti'[0]) # => S
print('Spaghetti'[4]) # => h

# python allows negative indexes
print('Spaghetti'[-1]) # => i
print('Spaghetti'[-4]) # => e

# python allows for ranged selections of strings
print("Spaghetti"[1:4]) # => pag
print("Spaghetti"[4:-1]) # => hett
print("Spaghetti"[4:4]) # => (empty string)

# short cut for beginning of string in range is to omit first num
print("Spaghetti"[:4])  # => Spag
print("Spaghetti"[:-1]) # => Spaghett

# same short cut for end of string, omit last num
print("Spaghetti"[1:])  # => Spag
print("Spaghetti"[-4:])    # => Spaghett

# indexing beyond the string provides an error
print("Spaghetti"[15])  # => Spag
print("Spaghetti"[-15])    # => Spaghett

# but ranges don't error
print("Spaghetti"[:15])    # => Spaghetti
print("Spaghetti"[15:])    # => (empty string)
print("Spaghetti"[-15:])    # => Spaghetti
print("Spaghetti"[:-15])    # => (empty string)
print("Spaghetti"[15:20])    # => (empty string)