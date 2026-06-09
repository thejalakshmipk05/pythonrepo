n = int(input())
temp = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

if temp == rev:
    print("Palindrome Number")
else:
    print("Not Palindrome")