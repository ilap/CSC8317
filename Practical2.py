__author__ = 'ilap'

# Task 1
print "Task 1"
from Bio import SeqIO
index = SeqIO.index("opsd.txt", "swiss")

# Task 2
#
print "Task 2"
print '\n'.join([s for s in index.keys() ])

#Task 3
print "Task 3"
print '\n'.join([s for s in sorted (index.keys()) ])

#Task 4
print "Task 4"
x = []
for obj in index.values():
    print 'AAAA', len (obj)
    x += [len (obj)]

n = len (index)
x_bar = sum(x)/n
print "Average", x_bar

#Task 5
print "Task 5"
sum_x_root = sum ([ x_i**2 for x_i in x])

s = (1/float(n-1))*(sum_x_root-n*x_bar**2)**(1/2.0)

print "Standard deviation is", s

#Task 6
print "Task 6"
for req in index.values ():
    print req.seq[9:30]


#Task 7
#'annotations', 'dbxrefs', 'description', 'features', 'format', 'id', 'letter_annotations', 'name', 'seq']
for vals in index.values():
    if vals.name == 'OPSD_HUMAN':
        aas = {}
        for aa in vals.seq:
            if aa not in aas:
                aas[aa] = 1
            else:
                aas[aa] += 1
        print aas

