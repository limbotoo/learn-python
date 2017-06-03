h=input('身高=')
w=input('体重=')
height=float(h)
weight=float(w)
bmi=weight/(height**2)
if bmi>32:
	print('严重肥胖')
elif bmi>28:
	print('肥胖')
elif bmi >25:
	print('过重')
elif bim>18.5:
	print('正常')
else:
	print('过轻')