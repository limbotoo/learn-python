def normalize(name):
	return name[:1].upper()+name[1:].lower()
l1=['adam','LISA','barT']
l2=list(map(normalize,l1))
print(l2)
		