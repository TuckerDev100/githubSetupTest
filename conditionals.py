# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 10


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

#simple if
# if x > y:
#     print(f'{x} is greater than {y}')

# #if else
# if x > y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{y} is greater than {x}')

#elif
# if x > y:
#     print(f'{x} is greater than {y}')
# elif x == y:
#      print(f'{y} is equal to {x}')

# else:
#     print(f'{y} is greater than {x}')

#Nested ifs
if x > 2:
    if x <= 10:
       print(f'{x} is greater than 2 and less than or equal to 10')


# Logical operators (and, or, not) - Used to combine conditional statements

if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or queal to 10  ')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object




# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
