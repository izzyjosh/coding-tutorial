#Classes and Inheritance
#import time

class Mammal:
	#name = "gabi"
	#age = 20
	
	def __init__(self,  name,  age, class1):
		self.name = name
		self.age = age
		self.class1 = class1
		
	def introduction(self, lang):
		return "My name is " + self.name + " and i am " + str(self.age) + " years old" + " in " +lang+ ' and am in ' + self.class1
	
	
mammal1 = Mammal("gabi",  16, 'jss3')
mammal2 = Mammal("mije",  4, 'jss3')
print(mammal2.name)
print(mammal1.name)
print(mammal1.age)
print(mammal1.introduction("python"))


class Math:
	def pow(self,  a,  b):
		return a ** b
		
	def abs(self,  a):
		# -3 and 5
		if a > 0:
			return a
		else:
			return a * -1
		

math = Math()
print(math.pow(2,  3))

print(math.abs(7))


# INHERITANCE

class HumanBeing(Mammal):
	def __init__(self,  name,  age, class1,  no_of_leg,  profession):
		super().__init__(name, age,  class1)
		self.leg = no_of_leg
		self.profession = profession
		
		
	def introduction(self, language):
		return "My name is " + self.name + " and i am " + str(self.age) + " years old" + ' in ' +language
			
			
human1 = HumanBeing("dev", 23, "jss3",  2,   "Programmer")
print(human1.introduction("html"))