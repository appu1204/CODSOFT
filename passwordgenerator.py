import random
import string
s1=string.ascii_uppercase
s2=string.ascii_lowercase
s3=string.digits
s4=string.punctuation

plen=int(input("enter the length of password : "))

s= []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
# print(s)
random.shuffle(s)
print("Your password is : ")
print("".join(s[0: plen]))
