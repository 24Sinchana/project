import random
letters=['a','b','ç','d','e','f','g','h','i','j','k','l','m','n','o','p','q','s','r','s','t','u','v',
         'w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T'
         'U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','&','*','+','(',')','%']
print("Welcome to password generator")
num_letters=int(input("How many letters you want in your password?"))
num_numbers=int(input("How many numbers you want in your password?"))
num_symbols=int(input("How many symbols you want in your password?"))        
password_list=[]
for i in range(1,num_letters+1):
    char=random.choice(letters)
    password_list+=char
    
for i in range(1,num_numbers+1):
    char=random.choice(numbers)
    password_list+=char
   
for i in range(1,num_symbols+1):
    char=random.choice(symbols)
    password_list+=char
    


random.shuffle(password_list)

password=""
for char in password_list:
    password += char
print("generated password is",password)
