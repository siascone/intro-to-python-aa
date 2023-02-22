# Logical AND
print(True and True) # => True
print(True and False) # => False
print(False and False) # => False

print(True or True) # => True
print(True or False) # => True
print(False or False) # => False


print(not True) # => False
print(not False and True) # => True
print(not True or False) # => False

# Python considers an object to be true (notice the lower case 't') UNLESS it is one of the following

    # constant: None or False
    # zero of any numeric type: 0, 0.0
    # empty sequence or collection
        # string: ''
        # list: []
        # tuple: ()
        # dictionary: {}
        # set()
        # range(0)
# In other words, all items in this list are False and everything else is true.