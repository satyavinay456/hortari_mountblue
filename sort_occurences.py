def sort_occurences(items):
	occurences_dict=[(i,items.count(i)) for i in items]
	fin_list=[i[0] for i in  sorted(occurences_dict,key=lambda a :(a[1],a[0]))]
	return fin_list

if __name__=='__main__':
	#input the numbers with delimiter as space
	print("enter the numbers with delilmiter as space")
	items=list(map(int,input().split()))
	print("items entered are :",items)
	print("After sorting : ",sort_occurences(items))
