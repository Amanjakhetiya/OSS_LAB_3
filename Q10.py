ana = {}
l = ["owl","ate","tea","arm","ram","low","kol","eat",]
for i in l:
	comp="".join(sorted(i))
	if comp in ana:
		ana[comp].append(i)
	else:
		ana[comp]=[]
		ana[comp].append(i)

print(list(ana.values()))
