import numpy as np
from operator import itemgetter

class Node:
	def __init__(self, name, weight, connects):
		self.name = name
		self.weight = weight
		self.connects = connects

with open('7input.txt','r') as file:
	lines = file.readlines()


parents = {}
nodes = {}
for line in lines:
	line = line.strip()
	name, weight, *connects = line.split(' ', 2)
	below = []
	if connects: 
		below = connects[0][3:].split(', ')
		for n in below:
			parents[n] = name
#(A node n consists of a value v and a list of references to other nodes.
# From wikipedia)
	nodes[name] = Node(name, int(weight[1:-1]), below)		

# n = next(iter(nodes))
# while n in parents:
# 	print(n)
# 	n = parents[n]
# print(n)

# 2eme partie
# prendre la racine de l'arbre
# regarder l'arborescence de chaque enfant
# calculer le poids total de chaque branches enfant

		

def Sum_weight(parent, MyList):
	MyList.append(nodes[parent].weight)
	for children in nodes[parent].connects:
		Sum_weight(nodes[parent].connects, MyList)
	# return sum(MyList)	

MyList = []
result = Sum_weight('lynvd', MyList)
# ListWeight = []	
# base = nodes['gynfwly'].connects
# for children in base:
# 	ListWeight.append(nodes[children].weight)
# 	n = next(iter(nodes[children]))
# 	while 



