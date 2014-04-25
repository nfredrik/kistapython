import os
import socket
import threading
import SocketServer

# http://stackoverflow.com/questions/18310152/sending-binary-data-over-sockets-with-python

UDS_PATH="#hwtestmgr"

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        #print "current_thread.name:", cur_thread.name
        #print "data:", data
        response = "{0}: {1}".format(cur_thread.name, data)
        self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.UnixStreamServer):
    pass

def register(agentId):
    bytes = bytearray()
    bytes.append(4)  # size
    bytes.append(MSG_REGISTER)
    bytes.append(agentId)

    return bytes

def done(agentId):
    bytes = bytearray()
    bytes.append(4)  # size
    bytes.append(MSG_REGISTER)
    bytes.append(agentId)
    bytes.append(FAULTCODE1)
    return bytes

def send_message(msg):
   sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(UDS_PATH)
    try:
        sock.sendall(msg)
    finally:
        sock.close()


def do_client_stuff():
    """
    When called, try to register to hwtestmgr.
    prepare to receive start-message
    wait a random time, i.e. simulate testing
    report back result to hwtestmgr 
    """
    register_msg = register(27)
    send_msg(register_msg)

    response = sock.recv(1024)

    time.sleep(2)

    done_msg = done(27) 
    send_msg(done_msg)



def client(ip, port, message):
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(UDS_PATH)
    try:
        sock.sendall(message)
        response = sock.recv(1024)
#        print "Received: {0}".format(response)
        print "Received: {0}".format(response)
    finally:
        sock.close()

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 0

    try:
        os.unlink(UDS_PATH)
    except:
        pass

    server = ThreadedTCPServer(UDS_PATH, ThreadedTCPRequestHandler)
    ip, port = 0, 0
    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name

    m_bytes = bytearray()
    m_bytes.aåppend(0x11)
    m_bytes.aåppend(022)
    client(ip, port, m_bytes)
#    client(ip, port, "Hello World 2")
#    client(ip, port, "Hello World 3")

    server.shutdown()
