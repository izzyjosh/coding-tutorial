# JSON => JavaScript Object Notation
import json


pyth_data = {
	1: {
		"name": "Michael Jøshua", 
		"age": 12,
		"stack": ["Python",  "JavaScript"], 
		"password": "1234"
	}, 
	2: {
		"name": "Joshua Michael", 
		"age": 16, 
		"stack": ["BASIC", "Python"], 
		"password": "0000"
	}, 
	3: {
		"name": "Zion Michael", 
		"age": 23, 
		"stack": ["HTML"], 
		"password": "2368"
	}
}

json_data = json.dumps(pyth_data, indent = 2,   ensure_ascii= False)
print(json_data)

print(json.loads(json_data))