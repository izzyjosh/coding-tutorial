name = input("names: ")
arr = [x.strip() for x in name.split(", ")]
print(arr)


for i, v in enumerate( range(10)):
	print(i+1, " : ", v)