#Python program to print a similar pattern as below:
#1
#22
#333

n = int(input('Enter a number: '))
for i in range(n):
    for j in range(i):
        print(i, end = '')
    print('')