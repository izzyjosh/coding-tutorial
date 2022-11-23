#from random import randint as r

file2 = open("/storage/emulated/0/coding tutorial/joshua.txt", "r")

#(file2.write('\n do u know me\n if yes \n say hi'))



#file2.close()

# Context Manager!!
#with open("/storage/emulated/0/coding tutorial/joshua.txt", "a") as file2:
#	file2.write('\n do u know me\n if yes \n say hi')
#	
#	
#print(r(1,  20))
print(file2.read())