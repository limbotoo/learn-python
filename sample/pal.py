def pal():
	return str(n)==str(n)[::-1]
output=filter(pal,range(100,999))
print(list(output))