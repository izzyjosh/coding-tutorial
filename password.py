import random
import time

alphabets = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "@#$%&?!/£¢€¥"


# uppercase,  lowercase,  numbers and symbols and length - 15

characters = alphabets + numbers + symbols + alphabets.upper()
choose_password = 0
while choose_password < 5:
	time.sleep(2)
	password = random.choices(characters,  k=8)
		
	output = ""
	for chr in password:
		output += chr
	print(output)
	choose_password += 1