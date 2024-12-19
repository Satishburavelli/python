username=input("Enter the username:")
password=input("Enter the password:")
a=len(username) >=5 and len(password) >=10
b= all(username[i:i+3] not in password for i in range(len(username) -2))
c=username[::-1] not in password
if a and b and c :
    print("True")
else:
    print("False") 
    