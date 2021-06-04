l1=[1,2,3,4]

#list comprehension

print([i**2 for i in l1],end='\n')

#using map
def func(x):
	return x**2
print(list(map(func,l1,)))