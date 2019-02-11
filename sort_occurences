def sort_occurences(items):
	occurences_dict=[(i,items.count(i)) for i in items]
	fin_list=[i[0] for i in  sorted(occurences_dict,key=lambda a :(a[1],a[0]))]
	return fin_list

if __name__=='__main__':
	items=[4, 5, 7, 7, 6, 5, 4, 3]
	print(sort_occurences(items))
