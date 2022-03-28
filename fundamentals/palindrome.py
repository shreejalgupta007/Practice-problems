#Write a code to check whether a given number is a palindrome.
a=input('Enter the number: ')

if a == a[::-1]:
    print("Yes its a palindrome")
else:
    print("No, its not a palindrome")