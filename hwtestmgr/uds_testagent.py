import socket
import sys
import time

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = './uds_socket'
print >>sys.stderr, 'connecting to %s' % server_address
try:
    sock.connect(server_address)
except socket.error, msg:
    print >>sys.stderr, msg
    sys.exit(1)


try:
    
    # Send data
    message = '@register:Kalle'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)
    print >>sys.stderr, 'go to sleep'    
    time.sleep(5)
    message = '@done:Kalle:fault'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
