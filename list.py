l1=['Hello','World','Apple',18,None]
l2=[s.lower() for s in l1 if isinstance(s,str)]
print(l2)