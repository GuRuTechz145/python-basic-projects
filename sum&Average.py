#Python program to find the sum and average(in float) of numbers given by a user
#The Program stops accepting input if 0 is entered

#initialize sum to be zero;
sum = 0;

i = 1;
while True:

    n = float(input('Enter a value or 0 to stop: '))
    if n == 0:
        break
    else:
        i +=1;
        sum +=n;
        avg = sum/(i-1);
        print(i-1)
        print('Sum: ' ,sum)
        print('Average: ' ,avg)
        


