import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    #host = input("enter ip")
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input("Hello would you like to play Tic Tak Toe? (y/n) \n")  # take input

    while 'winner' not in message.lower().strip():
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: \n' + data)  # show in terminal
        if('winner' in data.lower()):
            print('goodbye')
            break
        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
