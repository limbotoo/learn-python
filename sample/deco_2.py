import functools

def log(strorfunc):
	if isinstance(strorfunc,str):
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print('%s %s():'%(strorfunc,func.__name__))
				return func(*args,**kw)
			return wrapper
		return decorator
	else:
		@functools.wraps(strorfunc)
		def wrapper(*args,**kw):
			print('begin call %s():'%strorfunc.__name__)
			strorfunc(*args,**kw)
			print('end call %s():'%strorfunc.__name__)
		return wrapper
		
@log
def now():
	print('2017-6-2')
	
now()

@log('execute')
def now():
	print('2017-6-2')

now()