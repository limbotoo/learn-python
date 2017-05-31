from functools import reduce

def str2float(s):
	dot=s.find('.')
	times=len(s)-dot-1
	s=s.replace('.','')
	def fn(x,y):
		return x*10+y
		
	def char2num(s):
		return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

	l=reduce(fn,map(char2num,s))
	return l/(10*times)
print('str2float(\'123.456\')=',str2float('123.456'))