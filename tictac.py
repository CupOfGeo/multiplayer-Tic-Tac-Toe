'''
row 0| 1 ,2 ,3
row 1| 4 ,5 ,6
row 2| 7 ,8 ,9
col    c0|c1|c2
'''

board = [[1,2,3],
	 [4,5,6],
	 [7,8,9]]




def checkwin():
	for i in range(3):
		if(board[0][i] == board[1][i] == board[2][i]) and (not board[0][i] == ''):
			return board[0][i]# if found a win state return winner
		if(board[i][0] == board[i][1] == board[i][2]) and (not board[i][0] == ''):
			return board[i][0]

#diagonals
	if(board[0][0] == board[1][1] == board[2][2]) and (not board[1][1] == ''):
			return board[0][0]

	if(board[0][2] == board[1][1] == board[2][0]) and (not board[1][1] == ''):
			return board[0][i]
	return 'NO'


def checktaken(move): #check if the tile is open
	tile = board[move//3][move%3] 
	if(tile == 'x' or tile == 'o'):
		return False
	else:
		return True

def validMove(move): # chick if the input is valid
	if(move <= 8) and (move>= 0):
		return True
	else: 
		return False
	

def TicTakToe():
	#print(board[2][0])

	i = 0
	for i in range(9):
		print(board)
		move = int(input("1-9 move?"))
		move = move - 1
		while(checktaken(move) == False):
			move = int(input("that spot it already taken enter a new move")) -1

		while(validMove(move)== False):
			move = int(input("Thats not a spot please enter a number 1 - 9")) - 1

		if i%2 ==0:
			board[move//3][move%3] = 'x'
		else:
			board[move//3][move%3] = 'o'
		win = checkwin()
		if (win == 'x' or win == 'o'):
			break 

	print(win + " WINNER")
	return 1



if(__name__ == '__main__'):
	TicTakToe()


 
