import itertools
def divisibility(number):
	return [int("".join(i)) for i in itertools.permutations(number) if int(''.join(i))%8==0]

if __name__=='__main__':
	print("Enter the to check divisibility")
	number=input()
	print("You entered",number)
	print("All permutations of given digit that can be divisible by 8",divisibility(number))

