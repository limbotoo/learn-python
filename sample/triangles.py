def triangles():
	l=[1]
	while True:
		yield l
		l.append(0)
		l=[l[i-1]+l[i] for i in range (len (l))]
n=0
for m in triangles():
	print(m)
	n=n+1
	if n==10:
		break
