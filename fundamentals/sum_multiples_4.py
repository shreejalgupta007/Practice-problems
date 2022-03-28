#Write a code to find the sum of numbers divisible by 4.
# The code must allow the user to accept a number and 
# add it to the sum if it is divisible by 4. 
# It should continue accepting numbers as long as the user wants to provide an input and
# should display the final sum.
n=int(input('How many numbers you want to enter? '))
num=[]
for i in range(n):
    x=int(input('Enter number {}: '.format(i+1)))
    num.append(x)
sum=0
for j in num:
    if j%4==0:
        sum=sum+j
print('The sum of numbers divisible by 4 is',sum)