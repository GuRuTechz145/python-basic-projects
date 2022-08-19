#Python Program to tell if a letter is a vowel or consonant
from re import I


i = input('Give a letter of your choice: ');
if i in ('a', 'e', 'i', 'o', 'u') or i in ('A','E', 'I', 'O', 'U'):
    print(i, 'is a vowel')
    
    
elif i != ('a','e','i','o','u') or ('A','E','I','O','U'):
    print('is a consonant')
    
    
else:
    print('{} is a consonant'.format(i))
     