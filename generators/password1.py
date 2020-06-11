import string
from random import *

characters = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits
password = "".join(choice(characters) for i in range(randint(12,20)))

print(str(password))