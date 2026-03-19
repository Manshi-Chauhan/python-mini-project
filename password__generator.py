import random
import string 
letter=string.ascii_letters
digits = string.digits
symbols = string.punctuation
# pwd =random.sample(letter+digits+symbols,k=8)
#print(pwd)
# print("".join(pwd))
l=random.sample(letter,k=3)
d=random.sample(digits,k=3)
s=random.sample(symbols,k=3)
pwd=l+d+s
random.shuffle(pwd)
print("".join(pwd))
