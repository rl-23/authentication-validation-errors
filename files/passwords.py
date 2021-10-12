import os
'''
import csv

inputfile = open('users.csv')

with open('users.csv') as inputfile:
    reader = csv.reader(inputfile)
    inputm = dict(reader)

print(inputm)

passwordlist = []
usernamelist = []

'''
print("LOGIN SCREEN")
print("============")
print("Please enter your login details to access the system:\n")
count = 0

while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')

    if password=='letmein' and username=='Bob':
        print('Access Granted')
        break
    elif password=='password' and username=='Dave23':
        print('Access Granted')
        break
    elif password=='iloveben' and username=='Jenny99':
        print('Access Granted')
        break
    elif password=='s3cur3' and username=='Mark.Brown':
        print('Access Granted')
        break        
    elif password=='password123' and username=='big_mike_xx':
        print('Access Granted')
        break        
    else:
        print('Access denied. Try again.')
        count += 1

if count >= 3:
  #os.system('clear')
  print("locked out!!")

authenticated = False

print("LOGIN SCREEN")
print("============")
print("Please enter your login details to access the system:\n")

while not authenticated:
    username = input("Username > ")
    password = input("Password > ")

    authenticated = login_user(username, password)

    if not authenticated:
        print("\nI'm sorry, that is not a valid username/password combination. Please try again.\n")
      
  

os.system('clear')
print("Welcome to my program!")
print("======================")
print("Sadly, there's not much to do here. Bye!")

