#function
#codeblock
#three types of argument
#1)positional argument
#2)default argument
#3)keyword argument

def greet(name,  surname,  age=60):
	print("Hello %s"%name)
	print( "Hello %s"%name)
	
#	for i in range(10):
#		print(i)

	print("My name is " + name  + ' ' +  surname + " and  I am " + str(age) + " years old")
#	
#	
greet("Mike", age= 12,  surname= "Gabi")


#from guessing_game import level3,  level2

#level3()
#level2()