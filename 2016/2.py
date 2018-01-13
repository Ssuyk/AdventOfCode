def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# Program starts there
with open('2support.txt') as f:
    lines = f.readlines()

N= file_len('2support.txt')
S = 0
# ribbon = 0 #2nd part of the problem
for i in range(0,N):
	x_pos = [pos for pos, char in enumerate(lines[i]) if char == 'x']
	l_temp = float(lines[i][0:x_pos[0]])
	w_temp = float(lines[i][x_pos[0]+1:x_pos[1]])
	h_temp = float(lines[i][x_pos[1]+1:len(lines[i])])
	# D = [l_temp, w_temp, h_temp] #2nd part of the problem
	# D.sort() #2nd part of the problem
	# ribbon += 2*D[0]+2*D[1]+D[0]*D[1]*D[2] #2nd part of the problem
	lw_temp = l_temp*w_temp
	wh_temp = w_temp*h_temp
	lh_temp = l_temp*h_temp
	temp_min = min(lw_temp,wh_temp,lh_temp)
	S += 2*lw_temp+2*wh_temp+2*lh_temp+temp_min

print(ribbon)


