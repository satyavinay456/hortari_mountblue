import itertools
def divisibility(number):
	return [int("".join(i)) for i in set(itertools.permutations(number)) if (int(''.join(i))/8)%2==0]

if __name__=='__main__':
	print("Enter the number to check divisibility")
	number=input()
	print("You entered",number)
	print("All permutations of given digit that can be evenly divisible by 8 :",divisibility(number))
	if divisibility(number)==[]:
		print("Permutations of Entered number cannot be evenly divisible by 8")
	else:
		print("Permutations of Entered number can be evenly divisible by 8")
