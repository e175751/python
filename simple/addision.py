def add():
	x = 0
	s = 0
	for x in range(1,51):
		s += x
	print(s)

add()

print(sum(range(1,51)))

print(sum(x for x in range(1,51)))

#print(reduce(lambda x,y: x+y,range(1,51)))

print(50*51/2)


