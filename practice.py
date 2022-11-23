count = 0
cur = ""


while count < 6:
	user_input = input(">>> ")	
	if user_input == "":
		count = 0				
		cur = cur[:-1]
		cur = cur.zfill(6)
		print(cur[:2] + " hr " + cur[2:4] + " min " + cur[4:] + " sec ")
		count += 1	
	elif user_input.isdigit():
		cur += user_input
		max_digits = cur.zfill(6)
			
		time = max_digits[:2] + "hr " + max_digits[2:4] + "min " + max_digits[4:] + "sec"			
		print(time)
		
		count += 1

		
