import string
from random import *

length = input('otp length?')
ot = string.digits
otp = "".join(choice(ot) for i in range(int(length)))

print(otp)