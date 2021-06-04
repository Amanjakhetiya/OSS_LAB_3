def nearly_equal(a,b):
	if (abs(len(a)-len(b))>=2): return False
	if a==b: return True
	c=0
	a="".join(sorted(a))
	b="".join(sorted(b))
	for i,j in zip(a,b):
		if i!=j:
			c+=1

	return c<=1


print(nearly_equal("abcd","abcs"))
