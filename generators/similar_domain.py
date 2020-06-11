import string
import random
a =string.ascii_lowercase
def generate_random(name):
	name1=[]
	for i in name:
		if i in 'aeiou':
			name1.append(random.choice(a))
		else:
			name1.append(i)
	return ''.join(name1)
	


name = input('Enter name: ')
print(generate_random(name))