#A Pyhton Program to get the numbers from a given list that are divisble by another given number
#While testing for the divisible, if Python sees a value above 300,it should avoid it

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
    if n > 300:
        continue
    elif n%p == 0:
        print('{} is divisible by {}'.format(n, p))
    else:
        ('Ooops...Try next time')