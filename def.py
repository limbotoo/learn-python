import math
def quadratic(a,b,c):
	for i in [a,b,c]:
		if not isinstance(i,(int,float)):
			raise TypeError('bad operand type',i)

	deta=b**2-4*a*c
	if deta<0:
		print('方程无实根！')
	elif deta==0:
		x=(-b)/(2*a)
		print('方程有唯一解')
		return x
	else:
		x1=(-b+math.sqrt(deta))/(2*a)
		x2=(-b-math.sqrt(deta))/(2*a)
		print('方程有两个解')
		return x1,x2
print(quadratic(1,4,4))

