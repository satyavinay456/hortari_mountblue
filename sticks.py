sticks_cut=[]
#sticks=[5,4,4,2,2,8]
sticks=[1, 1, 2, 3]
sticks_cut.append(len(sticks))
while True:
	sticks=[i-min(sticks) for i in sticks if i-min(sticks)>0]
	if len(sticks)!=0:
		sticks_cut.append(len(sticks))
	if sticks==[] : break

print("final:",sticks)
print("cut: ",sticks_cut)