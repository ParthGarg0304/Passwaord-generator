#password generator
import random

char="abcdefghijklmnopqrstuvwxyzAQZWSXEDCVFRTGBNHYUJMKILOP1234567890!@#$%^&*_?|!?"

while True:
    password_len=int(input("What length would you like your password to be : "))
    password_count=int(input("How many passwords would you like : "))
    for i in range(0,password_count):
        password=""
        for j in range(0,password_len):
            password_char=random.choice(char)
            password+=password_char
        print("Here is your password : ",password)
