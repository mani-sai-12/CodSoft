import random
import string

length=int(input("Enter the length of the password: "))
lower=string.ascii_lowercase
upper=string.ascii_uppercase
number=string.digits
symbols=string.punctuation
 
all=lower+upper+number+symbols
temp=random.sample(all,length)
password="".join(temp)

print(password)