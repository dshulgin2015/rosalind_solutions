from itertools import permutations

def readGenome(filename):
    data = {}
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if line[0] == '>':
                data[next(f).rstrip()] = line.rstrip()
    return data

def overlap(a, b, min_length=2):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's suffx in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match

def naive_overlap_map(reads, k):
    olaps = []
    for a, b in permutations(reads, 2):
        olen = overlap(a, b, min_length=k)
        if olen >= 3:
            olaps.append((a, b))
    return olaps 

def print_result(list, data):
    res_str = ''
    for x in list:
        res_str = res_str + data[x[0]][1:] + ' ' + data[x[1]][1:] + '\n'
    print res_str

#reads = ['ACGGATC', 'GATCAAGT', 'TTCACGGA']
#print(naive_overlap_map(reads, 3).keys())
data = readGenome('GRPH.txt')
#print (naive_overlap_map(data.keys(), 3))

print_result(naive_overlap_map(data.keys(), 3),data)