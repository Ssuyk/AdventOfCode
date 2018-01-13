import numpy as np
import itertools

sum = 0
with open('input2.txt','r') as keyfile:
	for lines in keyfile.readlines():
		row_list = list(map(int,lines.split('\t')))
		for i in itertools.combinations(row_list, 2):
			if max(i) % min(i) == 0:
				sum += max(i) / min(i)
				break
		# Diff = np.max(row_list) - np.min(row_list)
		# sum += Diff
print(sum)
