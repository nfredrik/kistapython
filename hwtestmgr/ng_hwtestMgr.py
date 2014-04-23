import socket
import sys
import os

server_address = './uds_socket'

# Make sure the socket does not already exist
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)


# Bind the socket to the port
print >>sys.stderr, 'starting up on %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

test_agents = list()

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(20)

            if data == "" : continue

            print >>sys.stderr, 'received "%s"' % data
            if data.startswith('@'):

                message = data[1:].split(':')[0]  
                agentId = data[1:].split(':')[1]  
                if message == 'register':
                    if agentId not in test_agents:
                        test_agents.append(agentId)
                        print 'we now have following agents:', test_agents
                    else:
                        print >> sys.stderr, 'already registered'
                elif message == 'done':
                    if agentId in test_agents:
                        for i, itm in enumerate(test_agents):
                            del test_agents[i]
                            print 'deleting agent:', agentId
                    else:
                        print >> sys.stderr, 'not registered:', agentId                            
                else:
                    print >> sys.stderr, 'could not find message type!', message                    
            else:
                print >> sys.stderr, 'wrong starting token, expected:@, got%s:'%data[0]
                break
    finally:
        # Clean up the connection
        connection.close()
