#Palindrome number (3 digit)
num = int(input("Enter 3 digit number: "))

rev = (num % 10) * 100 + ((num // 10) % 10) * 10 + (num // 100)

if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
