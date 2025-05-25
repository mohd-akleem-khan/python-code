def info(firstname,lastname,**kargs):
	dict={'firstname':firstname,'lastname':lastname}
	for k,v in kargs.items():
		dict[k]=v
	return dict
result=info('akleem','khan',age=40,city='Lucknow')
print(result)
