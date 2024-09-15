num1 = 12
num2 = 3

ssum = num1 + num2
print('result', num1, '+', num2, 'is', ssum)

#----   with input   ----
val1 = input('input value 1 = ')
val2 = input('input value 2 = ')

sum2 = int(val1) + int(val2)
print('result', sum2,'\n')

#----   with function   ----

#create function and return value of a and b
def add(a,b):
    return a + b

#initializing the variables
num3 = 20
num4 = 15

#call the function and store the value into
sum_of_two_numbers = add(num3,num4)

#print the result
print('Sum of {0} and {1} is {2} \n' .format(num3,num4, sum_of_two_numbers))

#----   With operator.add()   ----

#import the operator module
import operator
su = operator.add(num1,num2)
print('result sum of {0} and {1} is {2}'.format(num1,num2,su))