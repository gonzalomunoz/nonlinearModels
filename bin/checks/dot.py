import matplotlib
matplotlib.use('Agg')
import graphviz as gv
import pylab

g1 = gv.Graph(format='png')

g1.node('A')
g1.node('B')
g1.edge('A', 'B')

#g1.view()
print(g1.source) 

filename = g1.render(filename='g1.dot')

pylab.savefig('filename.png')
