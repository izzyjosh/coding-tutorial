#tictactoe
moves = {
     "00":"",  
     "01":"",  
     "02":"",  
     "10":"",  
     "11":"",  
     "12":"", 
     "20":"" , 
     "21":"" , 
     "22":"" 
}

taken_spaces = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

def drawer():
	print(moves["00"] +"|"+moves["01"]+"|"+moves["02"])
	print("-+-+-")
	print(moves["10"]+"|"+moves["11"]+"|"+moves["12"])
	print("-+-+-")
	print(moves["20"]+"|"+moves["21"]+"|"+moves["22"])
	
sign = input("chose(X or O): ").lower()

def player1():
	marker = sign
	my_play = input(f"player1({marker}): ")
	moves[my_play] = marker
	taken_spaces[int(my_play[0])] [int(my_play[1])] = marker
	drawer()
	if taken_spaces[0][0] == taken_spaces[0][1] == taken_spaces[0][2] or taken_spaces[1][0] == taken_spaces[1][1] == taken_spaces[1][2] or taken_spaces[2][0] == taken_spaces[2][1]  == taken_spaces[2][2] or taken_spaces[0][0]  ==  taken_spaces[1][0] == taken_spaces[2][0] or taken_spaces[0][1] == taken_spaces[1][1] == taken_spaces[2][1] or taken_spaces[0][2] == taken_spaces[1][2] == taken_spaces[2][2] or taken_spaces[0][0] == taken_spaces[1][1] == taken_spaces[2][2] or taken_spaces[0][2] == taken_spaces[1][1] == taken_spaces[2][0]:
		print("player1 wins") 
		exit()
	
	
def player2():
	marker = "x" if sign == "o" else "o"
	my_play = input(f"player2({marker}): ")
	moves[my_play] = marker
	taken_spaces[int(my_play[0])] [int(my_play[1])] = marker
	drawer()
	if taken_spaces[0][0] == taken_spaces[0][1] == taken_spaces[0][2] or taken_spaces[1][0] == taken_spaces[1][1] == taken_spaces[1][2] or taken_spaces[2][0] == taken_spaces[2][1]  == taken_spaces[2][2] or taken_spaces[0][0]  ==  taken_spaces[1][0] == taken_spaces[2][0] or taken_spaces[0][1] == taken_spaces[1][1] == taken_spaces[2][1] or taken_spaces[0][2] == taken_spaces[1][2] == taken_spaces[2][2] or taken_spaces[0][0] == taken_spaces[1][1] == taken_spaces[2][2] or taken_spaces[0][2] == taken_spaces[1][1] == taken_spaces[2][0]:
		print("player2 wins")
		exit() 
		
def game():
	
	count = 0
	
	while count <9:
		
		player1()
		
		player2()
		count += 1
		print(count)
		
game()