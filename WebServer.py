#import socket module
from socket import *
import sys  # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM);
#Prepare a sever socket
#Fill in start
serverSocket.bind(('',8000));
serverSocket.listen(1);
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept();
    print("client socket is g");
    try:
        message =  connectionSocket.recv(1024);
        print(message,'::',message.split()[0],':',message.split()[1])
        filename = message.split()[1]
        print(filename,'||',filename[1:])
        f = open(filename[1:])
        outputdata =  f.read();
        print(outputdata);
        connectionSocket.sendall(b'HTTP/1.0 200 OK\r\n\r\n');
        #connectionSocket.sendall(outputdata);

        for i in range(0, len(outputdata)):
            connectionSocket.sendall(outputdata[i].encode('utf-8'));

        connectionSocket.close();

    except IOError:
        connectionSocket.send('404 Not Found');
        connectionSocket.close();
serverSocket.close();

sys.exit();
