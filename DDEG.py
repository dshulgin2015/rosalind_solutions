def readGraph(filename):
	with open(filename, 'r') as f:
		n, m = map(int, f.readline().strip().split())
		graph = [map(int, line.strip().split()) for line in f]
	return graph, n, m

graph, n, m = readGraph('data/deg.txt')

def dergee_list(n,graph):
	degrees = [0]*n
	for edge in graph:
		for node in edge:
			degrees[node-1]+=1
	return degrees

print ' '.join(map(str,dergee_list(n, graph)))