class Myclass:
	def __init__(self,name,age) :
		self.name=name
		self.age=age
		self.salary=0
	def display(self):
		print(f"name:{self.name} Age:{self.age}")
obj=Myclass("Akleem",30)
#obj.display()
print(obj.name)
print(obj.age)
print(obj.salary)
m1=Myclass('Amir Khan',60)
m1.display()
obj.age=85
obj.display()
