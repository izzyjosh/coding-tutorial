# HANDLING ERRORS

# ERRORS

"""
1. NameError
2. SyntaxError
3. ZeroDivisionError
4. TypeError
5. ValueError
6. IndentationError
7.AttributeError

"""

try:
	num1 = int(input('Num1: '))
	num2 = int(input('Num2: '))
	
	print(num1 / num2)
except ValueError:
	print('Enter a valid number')
except ZeroDivisionError:
	print('Enter a valid number greater than or less tham zero')
finally:
	print('Program Finished')