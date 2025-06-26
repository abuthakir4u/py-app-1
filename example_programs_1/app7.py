# Exception in Python

try:
    age = int(input('Age: ')) # this will throw exception when input is invalid number
    print(age)
    income = 2000
    test = income / age # this throws exception when age is 0
    print(test)
except ValueError:
    print('Invalid value found')
except ZeroDivisionError:
    print('Divide by zero exception occurred')

print ('done..')

# NOTE: Python uses # for comments

