# Exception and Error handling

# syntax error
# indentation error
# value error 
# logic error
#
#
#
#
#
# attribute error
# input error




# zero division error
"""
try:
    num = 6
    calc = num/0
    print(calc)
except ZeroDivisionError:
    print('Error found in the code')

# for value error
try:
    num=int('Enter a number: ')
    calc = num/3
    print(calc)
except ValueError:
    print('There is non integer in the input')
"""

# Index error
"""
try:
    my_list=[55,66,77,88,99]
    print(my_list[5])
except IndexError:
    print('There is an Indexing Error')

# Type error
try:
    num=input('Enter a number here: ')
    calc = 7/num
    print(num)
except TypeError:
    print('There is a Type error here')
"""

# Handling multiple Errors
""""
try:
    num1=5
    num2=int(input('Enter a number here: '))
    calc = num1/num2
    print(calc)
except ZeroDivisionError:
    print('There is zero at the denominator')
except ValueError:
    print('Wrong value, please change to a number')
else:
    print('No error in the code')
finally:
    print('Proceed to the next line of code')
    """

# else statement
"""
try: 
    num=0
    calc = 5/num
    print(calc)
except ZeroDivisionError:
    print('There is a zero at the denominator')
else:
    print('No error in the code')
"""

#indentation error
"""
try:
    i = 5
    if i > 2:
        print('Valid')
    else:
        print('Invalid')
except IndentationError:
    print('Indentation error detected')
"""


# COREY SCHAFER == YOUTUBE


"""
# ASSERTION ERROR AND RAISE ERROR

age = int(input('Enter your age'))
assert age >= 18, 'Age must be 18 0or older'
# assert 'condition', 'Outputs only if the condition is disobeyed'
print('You are eligible for a license')"
"""

try:
    Password = input('Enter Password:')
    if len(Password)>=7: 
        print('Proceed')
    else:
        raise Exception('Password length is too small, Make it 7 or greater than')
except Exception as e:
    print(e)

