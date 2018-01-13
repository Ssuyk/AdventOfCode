import numpy as np
import itertools

with open('input6.txt','r') as file:
	TempList = file.read().split(' ')
	List = np.zeros(16)
	j=0
	for char in TempList:
		if (char != ''):
			List[j] = int(char)
			j+=1

banks = [int(x) for x in List]

# count = 0
# seen = {}
# while tuple(banks) not in seen:
#     seen[tuple(banks)] = count
#     i, m = max(enumerate(banks), key=lambda k: (k[1], -k[0]))
#     banks[i] = 0
#     for j in itertools.islice(itertools.cycle(range(len(banks))), i + 1, i + m + 1):
#         banks[j] += 1
#     count += 1

# print(count)
# print(count - seen[tuple(banks)])

# en gros, tu trouves le max, puis tu
# redistribues a coup de -1 sur líntegralite de la liste
# en evitant l'indice du max. A chaque fois que tu as finis 
# la redistribution, tu verifies que la nouvelle configuration
# n'est pas déjà existante. Si ça existe, tu stop la boucle et 
# et tu affiches le nombre de tour de boucle effectue

index_final = 0
Hist_list = {}


# BoolValue = 1
while tuple(banks) not in Hist_list:
	Hist_list[tuple(banks)] = index_final
	Pos = np.argmax(banks)
	Temp_max = banks[Pos]
	for ind in range(1,int(Temp_max+1)):
		if (int((ind+Pos)%len(banks)) == Pos):
			pass
		else:
			banks[int((ind+Pos)%len(banks))]+=1
			banks[Pos]-=1
	index_final+=1

print(index_final)
print(index_final - Hist_list[tuple(banks)])		






