class Human:
	def __init__(self):
		pass
	def canWalk(self):
		print("Human can walk 10Km every day")
class Boy(Human):
	def __init__(self):
		self.gender='Male'
		self.walk=10
	def canWalk(self):
		super().canWalk()
		print(f"{self.gender} can walk {self.walk}Km")
b=Boy()
b.canWalk()

