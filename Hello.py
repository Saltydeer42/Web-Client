port = 80

import socket 

ip = socket.gethostbyname('www.bbc.com')
print ip

#for socket call (preparing to open the connection)
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#for connection
s.connect((ip, port))

#Send HTTP Request - look at `curl -v` for the part that starts with >
#The end of each line is actually "\r\n" - also known as CRLF for carriage return line feed

s.send('GET / HTTP/1.1\r\n')
s.send('user-agent: Teddy\r\n')
s.send('host: www.bbc.com\r\n')
s.send('Connection: close\r\n')
s.send('Accept-Encoding: identity\r\n')
s.send('\r\n')


#End of request is just an plain "\r\n"

#Read response and print to screen

chunks = []
bytes_recd = 0
chunk = 'a'
while chunk != '':
	chunk = s.recv(2048)
	chunks.append(chunk)
	bytes_recd = bytes_recd + len(chunk)
print ''.join(chunks)

import requests
