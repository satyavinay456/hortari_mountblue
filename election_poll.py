def election_polls(names_list):
	occurences_dict=dict((i,names_list.count(i)) for i in set(names_list))
	return sorted([name for name,count in occurences_dict.items() if count==max(occurences_dict.values())],key=lambda x:x.lower())[-1]	

if __name__=='__main__':
	#input the voters with delimiter as space
	print("enter the names with delilmiter as space")
	votes=list(map(str,input().split()))
	print("voters list : ",votes)
	print(election_polls(votes),"wins")
