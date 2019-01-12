def judgeCircle(moves):
	x = y = 0
	for move in moves:
		if move == "U":
			y=y+1
		elif move == "D":
			y=y-1
		elif move == "L":
			x=x+1
		elif move == "R":
			x=x-1
	if x==0 and y==0:
		return True
	else:
		return False

if __name__== "__main__":
	print(judgeCircle("UD"))
	print(judgeCircle("LL"))