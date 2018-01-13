

with open('5input.txt') as file:
	List = list(map(int,file.readlines()))
	# print(int(List[1]))
	pos = 0	
	step = 0
	On = True

try:
	while On:
		# print(step)
		if (pos>=0) or (pos<len(List)):
			step+=1
			if List[pos]>=3:
				List[pos]-=1
				pos+=List[pos]+1
			else:
				List[pos]+=1
				pos+=List[pos]-1
		else:
			On = False	

except IndexError:
    pass

print(step-1)