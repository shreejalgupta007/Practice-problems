#Write a code to find the minimum among three given numbers.

a=int(input('Enter first number'))
b=int(input('Enter second number'))
c=int(input('Enter third number'))
if a<=b and a<=c:
    min=a
elif b<=a and b<=c:
    min=b
else:
    min=c
print('The minimum number among {}, {}, {} is {}.'.format(a,b,c,min))
