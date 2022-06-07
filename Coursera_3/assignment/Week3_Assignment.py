import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #think of mysock as a file handler
mysock.connect(('data.pr4e.org', 80)) #connect to that socket that can reach to domain and port 80
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
#encodes the string using the specified encoding
mysock.send(cmd)
#sending that data to server and server reads through the files and sending the data back

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
# we are receiving up to 512 bytes; if we get no file, then break
# if we get data, then decode it; converts the code to internal format
mysock.close()