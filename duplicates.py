def duplicates(items):
	non_duplic=[]
	for i in items:
		if i not in non_duplic:
			non_duplic.append(i)
	return non_duplic

if __name__=='__main__':
	items= [4, 5, 5, 6, 6, 6]
	print(duplicates(items))
