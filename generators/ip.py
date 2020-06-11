import random

ip = ".".join(str(random.randint(0,255)) for i in range(4))
print(ip)