import socket

host = socket.gethostname()

port = 1234

clientSocketFile = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocketFile.connect((host, port))



clientSocketFile.sendall(b'Hello, Teck')

print(clientSocketFile.recv(50))

clientSocketFile.close()


