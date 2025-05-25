with open('sample.txt','r') as file_obj:
	#content=file_obj.read()
	#print(content)
	#for data in file_obj:
		#print(data.rstrip())
	datalist=file_obj.readlines()
	for data in datalist:
		print(data.rstrip())
	#print(datalist)
