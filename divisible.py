#Python Program to get numbers from a given list that are divisble by another given numbers

p = int(input('Give a number to find the dividends: '))
list = [];

while True:
    i = input('Enter a number you want in the list or press q to quit: ')
    if i == 'q':
       break

    else:
        k = int(i);
        list.append(k);
print('For this list: {}'.format(list))


for n in list:
    if n%p == 0:
        print('{} is divisible by {}'.format(n, p))
    else:
        ('Ooops...Try next time')
        
        
        
        
        
        
        
        
