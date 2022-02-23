
import random
import string

print("Welcome to Password Generator")
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
characters = string.punctuation

char = upper + lower + digits + characters

number = int(input("Enter the number of passwords you want: "))
password_len = int(input("Enter the maximum length of the password: "))

print("\nThese are your passwords: ")

for pwd in range(1, number + 1):
    passwords = ""
    for i in range(1, password_len + 1):
        passwords += random.choice(char)
    print(passwords)
