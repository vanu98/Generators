import string
from random import *

remember = input('Enter a familiar words: ')
length = len(remember)
characters= string.punctuation + string.digits
password = remember[:3]
password += "".join(choice(characters) for i in range(randint(8,12)))
print(password)