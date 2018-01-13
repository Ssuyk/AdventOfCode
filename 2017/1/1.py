'''
Advent of code 2017 Day 1 
'''

with open('input1.txt', 'r') as keyfile:
    keylist = list(map(int, keyfile.read().strip()))
    print(len(keylist))
    sum = 0

    # for i in range(len(keylist)):
    # 	if(keylist[i] == keylist[i-1]):
    # 		sum += keylist[i]
    N = len(keylist)
    for i in range(N):
    	if ((i > int(N/2-1)) and (keylist[i] == keylist[i - int(N/2)])):
    		sum += keylist[i]
    	elif ((i <= int(N/2-1)) and (keylist[i] == keylist[i + int(N/2)])):
    		sum += keylist[i]
print(sum)