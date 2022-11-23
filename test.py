from decorators import operation
from decorators import star, percent
@operation
def number(a):
	pass
	
number(-76)


@star
@percent
def name(a):
	print(a)
name("joshua joseph")