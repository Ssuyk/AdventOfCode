import numpy as np
from collections import Counter

def is_anagram(str1, str2):
     return Counter(str1) == Counter(str2)

def isValid(line):
	for i in itertools.combinations(line.rstrip('\n').split(' '), 2):
		if (i[0]==i[1]) or (is_anagram(i[0], i[1])):
			return False 
			break
			# print('equal')
	return True		


ind = 0
with open('4input.txt') as file:
	List = file.readlines()
	for lines in List:
		if isValid(lines):
			ind+=1

print(ind)