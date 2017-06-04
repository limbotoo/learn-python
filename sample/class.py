'a class'

__author__='limbotoo'

class boy(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age
		
	def print_age(self):
		print('%s:%s'%(self.name,self.age))
		
	def old(self):
		if self.age>=70:
			print('old')
		elif self.age>=40:
			print('adult')
		elif self.age>=18:
			print('young')
		else:
			print('teenager')
			
tangh=boy('Tom',24)

tangh.print_age()
tangh.old()


