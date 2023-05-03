'''
write a program that asks the user to provide his name and his email using input , then do the following:
Check that the name length is more than 2 characters.
Check that the email is valid (using string operations and coditionals)
You only accept @gmail emails .
if the email is valid, display a welcome message to the user . for example :
welcome Ahmed, you registered with the email ahmed@gmail.com !

if the email or name is not valid, display the message :
 the email is not valid , please provide a valid email .
or

the name length must be more than 2 characters, please provide a valid name.
'''
username = input("Please inter your name: ")
email = input("Please inter your email: ")

if username.__len__() > 2:
  #  if "@gmail.com"in email and email.isspace():
    if email.endswith("@gmail.com"):
        print(f"welcome {username}, you registered with the email {email} !")
    else:
        print("the email is not valid , please provide a valid email.")
else:
    print("the name length must be more than 2 characters, please provide a valid name")
