import re

def parse_csv(a,delim):
	return list(re.split('['+(" ".join(delim))+']',a))

a="My;name;is,aman!jakhetiya"
print(parse_csv(a,[';',',','!']))

