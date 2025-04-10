password=input("Enter password: ")
if(len(password)>=8 and
   any(c.islower() for c in password) and
   any(c.isupper() for c in password) and
   any(c.isdigit() for c in password) and
   any(c in "!@#$%^&*(){}[]|\<>/?" for c in password)):
       print(f"{password} is strong")
else:
       print("Password is weak")
