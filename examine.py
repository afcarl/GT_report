from collections import defaultdict
from random import shuffle

train_ratio = 0.7
vertices = []
edges = []
with open('karate_network.csv') as f:
    for line in f:
        v1, v2 = line.rstrip('\n').split(' ')
        v1 = int(v1)
        v2 = int(v2)
        edges.append((v1, v2))
        if v1 not in vertices:
            vertices.append(v1)
        if v2 not in vertices:
            vertices.append(v2)

cut_off = int(train_ratio*len(edges))
shuffle(edges)
train_network = edges[:cut_off]
test_network = edges[cut_off:]

print 'All the vertices'
print vertices
print ''
print '# of undirected edges'
print len(edges)
print ''
print 'Train edges'
print train_network
print ''
print 'Test edges'
print test_network
print ''


T_matrix = defaultdict(lambda: defaultdict(int))
for e in train_network:
    T_matrix[e[0]][e[1]] = 1
    T_matrix[e[1]][e[0]] = 1

print 'Transfer Matrix'
for v1 in xrange(1, len(vertices)+1):
    out = []
    for v2 in xrange(1, len(vertices)+1):
        if v1 in T_matrix and v2 in T_matrix[v1]:
            out.append('1')
        else:
            out.append('0')
    print ' '.join(out)
print ''

# solution 
steps = 3
solution_matrix = []
for v0 in vertices:
    final_vector = [ 0. for _ in xrange(len(vertices)+1) ]
    for step in xrange(1, steps+1):
        base_vector = [ 0. for _ in xrange(len(vertices)+1) ]
        tran_vector = [ 0. for _ in xrange(len(vertices)+1) ]
        base_vector[v0] = 1
        tran_vector[v0] = 1
        for s in xrange(step):
            base_vector = tran_vector[:]
            tran_vector = [ 0. for _ in xrange(len(vertices)+1) ]
            for v1 in xrange(len(vertices)+1):
                if base_vector[v1] != 0. and v1 in T_matrix:
                    branch = float( len(T_matrix[v1]) )
                    for v2 in xrange(len(vertices)+1):
                        if v2 in T_matrix[v1]:
                            tran_vector[v2] += base_vector[v1]/branch
        for idx in xrange(len(vertices)+1):
            final_vector[idx] += base_vector[idx]
    solution_matrix.append( final_vector )
    #print v0, ' '.join(map(str, final_vector))

print 'Solution Matrix'
for col, vec in enumerate(solution_matrix, 1):
    print '[', col, ']', ' '.join(map(str, vec[1:]))
print ''





