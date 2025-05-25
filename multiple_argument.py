def add(x,*args):
	sum=x
	for a in args:
		sum=sum+a
	return sum
result=add(2,3,5)
print(result)
result=add(2)
print(result)
