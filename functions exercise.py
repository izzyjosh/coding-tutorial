#functions
#write a python function to find the max of three numbers 
list1 = [1, 5, 8, 56, 54, 22, 97, 146, 66, 805, 23, 54]


def max_number(number):
	largest_number = list1[0]
	for i in number:
		if i > largest_number:
			largest_number = i
	print(largest_number)
			
max_number(list1)

#write a python program to sum all the numbers in a list


list2 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]

def sum(num):
	total = 0
	for a in num:
		total = total + a
		
	return total
	
print(sum(list2))

# write a python function to multiply numbers in a list

list3 = [1, 3, 4, 5, 6, 7, -8, 9]
def product(numbers):
	number = 1
	for i in numbers:
		number = number * i
	return number
	
print(product(list3))


#write a python program to reverse a string

name = "joshua"

def rev(names):
	arr = []
	for i in names:
		arr.append(i)
	arr.reverse()
	output = ""
	for j in arr:
		output += j
		
	return(output)
	
print('the reverse of joshua is , ', rev(name))


#write a python program to check if a number falls in a given range

number1 = int(input('Enter a number: '))
def rang(n):
	if n in range(12):
		print(True)
	else:
		print(False)
			
rang(number1)	


#write a python program that calculate the number of upper case letter and lower case letter and return the answer

#name2 = 'JoshUA'
#def upper_lower(name3):
#	upper = 0
#	lower = 0
#	for n in name3:
#		if n == name3[int(n)].lower():
#			upper += 1
#		elif n == name3[int(n)].upper():
#			lower += 1
#	
#			
#upper_lower(name2)



			