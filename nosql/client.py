import socket
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCKET.connect(('localhost', 50505))
SOCKET.send('PUTLIST;bar;a,b,c;LIST')

sleep(1)

SOCKET.send('"STATS;;;"')
