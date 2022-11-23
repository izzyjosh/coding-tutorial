def lcm(a, b):
	# case1 => a > b and a/b rem == 0
	if a > b and a % b == 0:
		return a
	# case2 => b > a and b/a rem == 0
	elif b > a and b % a == 0:
		return b
	# case3 => 
	else:
		for i in range(a,  a*b):
			if i % a == 0 and i % b == 0:
				return i
	
	
print(lcm(2, 4))


def lcm(a, b, c):
	if a > b and a > c and a % b ==  0 and a % c == 0:
			return a
			
	elif b > c and b > a and  b % c == 0 and b % a == 0:
			return b
			
	elif c > a and c > b and c % a == 0 and c % b == 0:
			return c
			
	else:
		for i in range (a, a*b*c):
			if i % a == 0 and i % b == 0 and i % c == 0:
				return i
		
		
print(lcm(12, 8, 16))

