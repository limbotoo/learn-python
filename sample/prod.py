from functools import reduce

def prod(l):
	def f(x,y):
		return x*y
	return reduce(f,l)
print('3*5*7*9=',prod([3,5,7,9]))