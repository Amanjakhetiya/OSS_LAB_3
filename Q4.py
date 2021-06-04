l1=[1,2,3,4]

#list Comprehension

print([x for x in l1 if x%2==0])

#filter

print(list(filter(lambda x:x%2==0,l1)))