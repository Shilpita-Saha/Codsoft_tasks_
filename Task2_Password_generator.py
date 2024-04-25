import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['!','@','#','$','%','^','&','*','(',')']
numbers=['0','1','2','3','4','5','6','7','8','9']
print("WELCOME TO THE PASSWORD GENERATIOR")
no_letters=int(input("How many letters you want in your password?"))
no_symbols=int(input("How many symbols you want in your password?"))
no_numbers=int(input("How many numbers you want in your password?"))
password=""
for i in range(1,no_letters+1):
    char=random.choice(letters)
    password=password+char
for i in range(1,no_symbols+1):
    char=random.choice(symbols)
    password=password+char
for i in range(1,no_numbers+1):
    char=random.choice(numbers)
    password=password+char
print(password)
    
