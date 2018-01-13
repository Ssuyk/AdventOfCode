My_File = open('1support.txt','r')
Floor = 0
ind = 0#Extra for second part of problem
for char in My_File.read():
	if char == '(':
		Floor +=1
	elif char == ')':
		Floor -=1
	ind+=1	#Extra for second part of problem
	if Floor == -1: #Extra for second part of problem
		break	#Extra for second part of problem

print(Floor)
print(ind)#Extra for second part of problem


