#input the sticks with delimiter as space
print("enter the sticks with delilmiter as space")
sticks=list(map(int,input().split()))
print("sticks entered : ",sticks)

sticks_cut=[]
sticks_cut.append(len(sticks))

while True:
	sticks=[i-min(sticks) for i in sticks if i-min(sticks)>0]
	if len(sticks)!=0:
		sticks_cut.append(len(sticks))
	if sticks==[] : break

print("list of number of sticks you had at the start of each turn: ",sticks_cut)
