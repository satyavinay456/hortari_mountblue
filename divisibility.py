import itertools
def divisibility(number):
	print(["".join(i) for i in itertools.permutations(number)])
	return [int("".join(i)) for i in itertools.permutations(number) if int(''.join(i))%8==0]

if __name__=='__main__':
	number='123'
	print(divisibility(number))

