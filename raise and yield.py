# raise and yield(generators)
from keyword import kwlist


file_type = ["jpg",  "png"]
# .jkj

#img = input(">>> ")

#if img.split(".")[-1] in file_type:
#	print("Saved!!!")
#else:
#	raise ValueError(f"{img} format cannot be accepted")
#	
	

def gen(num):
	for i in range(num):
		yield i
		
		
#for i in gen(6):
#	print(i)

g1 = gen(6)

try:
	print(next(g1))
	print(next(g1))
	print(next(g1))
	print(next(g1))
	print(next(g1))
	print(next(g1))
	print(next(g1))
	print(next(g1))
except:
	pass

	
print(kwlist)	