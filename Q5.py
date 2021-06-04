def triplets(n):
	ans=[]
	for i in range(1,n):
		for j in range(i+1,n):
			if i+j<=n:
				ans.append([i,j,i+j])

	print(ans)

triplets(8)