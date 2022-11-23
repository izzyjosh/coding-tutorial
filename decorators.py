def name(name):
	def inner():
		print("_"*5)
		name()
		print("_"*5)
	return inner
	
	
#@name	
#def nam():
#	print("jishua")
#	
#nam()



def num(func):
	def div(a, b):
		print("i am going to divide ", a, " and", b)
		if b == 0:
			print("oops this is not possible")
			return
		
		func(a, b)
		print("i am going to divide ", a, " and", b)
	return div
	
#@num
#def divide(a, b):
#	print(a/b)
#	
#divide(2, 7)

			

def work(func):
	def inner(*args, **kwargs):
		print("i can decorate all")
		
		return func(*args, **kwargs)
	return inner
	
#@work
#def name(n):
#	print(n)
#	
#name("joshua")

def star(func):
	def inner(a, **kwargs):
		print("*"*10)
		func(a, **kwargs)
		print("*"*10)
	return inner
	
def percent(func):
	def inner(a, **kwargs):
		print("%"*10)
		func(a, **kwargs)
		print("%"*10)
	return inner
	
	
#@star
#@percent
#def name(n):
#	print(n)
#name('joshua')

#names = input("name")
#name(names)



def operation(func):
	def inner(a):
		if a < 0:
			print("number is negative")
			return
		else:
			print("number is positive")
			return
		func(a)
	return inner
	
#@operation
#def number(num):
#	return num
#	
#number(97)