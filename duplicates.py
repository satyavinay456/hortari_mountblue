def duplicates(items):
	non_duplic=[]
	for i in items:
		if i not in non_duplic:
			non_duplic.append(i)
	return non_duplic

if __name__=='__main__':
	#input the numbers with delimiter as space
	print("Enter the numbers with delilmiter as space")
	items=list(map(int,input().split()))
	print("Items entered are :",items)
	print("After removing duplicates :",duplicates(items))
