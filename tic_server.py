import socket


def checkwin(board):
        for i in range(3): #ROWS and COLS check
                if(board[0][i] == board[1][i] == board[2][i]) and (not board[0][i] == ''):
                        return board[0][i]# if found a win state return winner
                if(board[i][0] == board[i][1] == board[i][2]) and (not board[i][0] == ''):
                        return board[i][0]

#diagonals
        if(board[0][0] == board[1][1] == board[2][2]) and (not board[1][1] == ''):
                        return board[0][0]

        if(board[0][2] == board[1][1] == board[2][0]) and (not board[1][1] == ''):
                        return board[0][i]
        return 'NO ONE'


def checktaken(move,board): #check if the tile is open
        tile = board[move//3][move%3]
        if(tile == 'x' or tile == 'o'):
                return False
        else:
                return True

def validMove(move,b): # chick if the input is valid
        if(move <= 8) and (move>= 0) and checktaken(move,b):
                return True
        else:
                return False

def board2str(board):
        return ('\n'.join(map(str,board)))    


def server_program():
    board= [[1,2,3],[4,5,6],[7,8,9]]

    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    i = 0 #Even will be Client move odd will be Server move

    while True and i < 8: #only 9 valid moves in tic tac toe at most 
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        if(str(data) == 'y'): # first move goes to user
            prompt = board2str(board) + "\nEnter a move 1-9: "
            conn.send(prompt.encode())
            continue
        
        move = int(data) - 1
        if(validMove(move,board)== False): # if recived an invalid move
            prompt = "That is not a valid spot please try again "
            conn.send(prompt.encode()) # prompt for a valid move
            continue #continue back to the top of the while loop 

        else: # was a valid move
            board[move//3][move%3] = 'o'#add move to the board
            win = checkwin(board)
            if(win == 'x' or win =='o'): #win condition
                print(board2str(board) + "\n WINNER " + win)
                prompt = "WINNER" + board2str(board)
                conn.send(prompt.encode()) # <---------SENDING MESSAGE TO CLIENT
                conn.close()#<-------------------------CLOSING SOCKET
                return
            print(board2str(board))
            i = i +1 #add clints turn to counter	


        
        if(i%2 ==1): # Odd Server move
            move = input('1-9 move -> ')
            move = int(move) - 1
            while(validMove(move,board)== False): # prompt for valid move
                move = int(input("Thats not a valid spot please enter a number 1 - 9")) - 1

            board[move//3][move%3] = 'x' #add move to board
            win = checkwin(board) #check winner
            if(win == 'x' or win =='o'):
                winText = (str(board) + " \n WINNER is " + win)
                conn.send(winText.encode())
            else:
                i = i + 1 #End of servers turn  
                prompt = board2str(board) + "\n Enter a move 1-9: "
                conn.send(prompt.encode()) # send board and prompt to enter a new move


    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()

