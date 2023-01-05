#5
#44
#333
#2222
#11111 



#sum = 1
#word =
#word.reverse()
#for i in word:
#	print(str(i) * sum)
#	
#	
#	sum += 1

#string  = "5, 4, 3, 2, 1"	
#times = 1
#for i in range(5, 0, -1):
#	for j in range(i):
#		print(j * times )
#		
#		times += 1		

#n = 5
#for i in range(n,  0,  -1):
#	output = ""
#	for j in range(i,  n+1):
#		#output += str(i)
#		print(i,  end="")
#	print()
#	
	
#n = 5
#for i in range(1, 6):
#	for j in range(i, n+1):
#		print(i, end="")
#	print()
	
	

#	
#for i in range(1, 6):
#	for j in range(i):
#		print(i, end="")
#	print()
	
	
#5
#45
#345
#2345
#12345
#n = 5
#for i in range(n, 0, -1):
#	for j in range(i, n+1):
#		print(j, end= "")
#	print()

	
		
			
'''
1
121
12321
1234321
123454321
'''

#for i in range(1, 6):
#	for j in range(1, i+1):
#		print(j, end="")
#		if j == i:
#			for k in range(i-1, 0, -1):
#				print(k, end = "")
#	print()

#00hr, 00min, 00sec
#()
#cur = ""
#while len(cur) < 6:
#	user_input = input(">>> ")
#	cur += user_input
#	max_digits = cur.zfill(6)
#	
#	time = max_digits[:2] + "hr " + max_digits[2:4] + "min " + max_digits[4:] + "sec"
#	
#	
#	print(time)
#	
#	
#	
#	
#	
#count = 0
#while count < 6:	
#	word = [i for i in cur]
#	output = ""
#	delete = input("del to delete: ")
#	if delete == "del":
#		word.remove(word[-1])
#		word.insert(0, 0)
#		for i in word:
#			output += str(i)
#		cur = output
#		print(output[:2] + " hr " + output[2:4] + " min " + output[4:] + " sec ")
#		count += 1
#		
		
#name = "674532"
#print(name)
#while int(name) != 0:
#	user_input = input(">>> ")
#	name = name[:-1]
#	name = name.zfill(6)
#	print(name)
#	
	
#acc_bal = 30000
#while acc_bal != 0:
#	print('''
#debit alert:
#amount: 5000 naira''')
#	acc_bal -= 5000
#if acc_bal == 0:
#	print("your account balance is currently empty")


#word = input(">>> ")
#output = ""
#for i in word[:-5]:
#	output += "*"
#print( output + word[-5:])



#word = input("enter sentence: ")
#upper = 0
#lower = 0
#for i in word:
#	if i.isupper():
#		upper += 1
#	elif i.islower():
#		lower += 1
#		
#		
#print(upper)
#print(lower)

#def num(a, b, c):
#	print(True if str(a*b)[-1] == str(c)[-1] else False)
#num(4, 5, 0)

#numbers = int(input("number: "))
#def factors(x):
#	print([i for i in range(1, x+1) if x % i == 0])
#	
#factors(numbers)



#file = open("/storage/emulated/0/coding tutorial/exercise.py", "r")
#newFile = open("/storage/emulated/0/mycode/copy2.py", "w")

#fileContent = file.read()

#newFile.write(fileContent)

#newFile.close()

#file.close()	



#import json
#word = input("sentence: ")
#my_dict = {}

#word = []

#for i in word:
#	if i not in word:
#		word.append(i)
#		
#for i in word:
#	my_dict.update({i : word.count(i)})
#	
#json_dict = json.dumps(my_dict, indent = 2)
#print(json_dict)


#f#or i in word:
#	my_dict[i] = word.count(i)
#	
#print(my_dict)


#import json
#with open ("/storage/emulated/0/coding tutorial/read.txt", "r") as file:
#	file1 = file.read()
#	
#	
#db ={}
#word =[]	
#for i in file1.split("\n"):
#	for j in i.split(" "):
#		word.append(j.strip())
#print(word)



#for i in word:
#	db[i] = word.count(i)
#	
#json_db = json.dumps(db, indent = 2)
#print(json_db)


#def c(speed):
#	if speed <= 70:
#		print("ok")
#	elif speed <= 130:
#		extraspeed = speed - 70
#		print("points:" , int(extraspeed/5))
#	else:
#		print("license suspended")
#			
#		
#c(170)

#word = input("enter word: ")
#def has_no_e(word):
#	for i in word:
#		if i == "e":
#			print(False)
#			break
#		
#	else:
#		print(True)

#has_no_e(word)


#def has_no_e(word):
#	word = word.split(" ")
#	word_without_e = []
#	for i in word:
#		if "e" not in word[word.index(i)]:
#			word_without_e.append(i)
#	percentage_of_word_without_e = int((len(word_without_e)/len(word)) * 100)
#	print("percentage of word without e =  " + str(percentage_of_word_without_e) + "%")
#		
#has_no_e(word)


 
#word = input("sentence: ")
#word = word.split()
#output = ""
#for i in word:
#	new_word = i[1:len(i)]+i[0]+"ay"
#	output += new_word +" "
#print(output)


#name = input("filename: ")
#print(name.split(".")[-1])




def pattern():
	count = 0
	space = 0
	while count < 30:
		if count <15:
			print(space* " ", 15*"*")
			space += 1
			count += 1
		elif count >= 15:
			print(space*" ", 15*"*")
			space -=1
			count += 1
			
count = 0
while count <2:			
	pattern()
	count += 1
#	
	
#stop = 20
#for _ in range(10):
#	start = 8
#	for i in range(start+1, stop):
#		if i > 8:
#			print(" " * (i-8), end= f"{8*'*'}")
#			print()
#		else:
#			print("*" * 8)
#		if i == stop - 1:
#			for j in range(stop, 7, -1):
#				if i > 8:
#					print(" " * (j-8), end= f"{8*'*'}")
#					print()
#				else:
#					print("*" * 8)

#number = int(input("number: "))
#output = ""
#for i in  range(1, number+1):
#	if number % i== 0:
#		output += str(i)
#	
#print("number is prime" if output == f"1{number}" else "number is not prime")




#pattern printing on harsh#

num = 30
count = 1
space = num -1

while count <= num:
	print(space * " "+count * "#")
	count += 1
	space -= 1

	
		
number = 1	
for i in range(29, 0, -1):
		print(i*" "+ number *"#")
		number += 1