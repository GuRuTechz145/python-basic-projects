#Python program that accepts two inputs(integer) from a user. 
#If the sum of the numbers is between 40 and 60, Python should report this and otherwise, should print the sum of the two numbers.

sum = 0;
i = int(input('Enter a number: '))
j = int(input('Enter a number: '))

sum = i + j;

if sum >= 40 and sum <= 60:
    print('Somewhere between 40 and 60')
else:
    print('The sum of {} and {} is {}'.format(i, j, sum))
    
    
    
    