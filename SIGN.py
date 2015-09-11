from itertools import permutations, product

def plusAndMinusPermutations(items):
    for p in permutations(items):
        for signs in product([-1,1], repeat=len(items)):
            yield [a*sign for a,sign in zip(p,signs)]

def print_result(list):
	for x in list:
		i = 0
		while i < len(x):
			print str(x[i]),
			i += 1
		print '\n'

print len(list( plusAndMinusPermutations(range(1,5)) ))

print_result(list( plusAndMinusPermutations(range(1,5)) ))