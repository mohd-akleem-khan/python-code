from name import formatted_name
print('Enter q to terminated')
while True:
	first=input('Enter first name ')
	if first =='q':
		break
	last=input('Enter second name ')
	if last=='q':
		break
	fname=formatted_name(first,last)
	print(fname)
