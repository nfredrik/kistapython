import sys
import time
import socket
from random import randrange

def get_conn():
    #time.sleep(0.1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 50505))
    return s

def send_string(st, debug=False):
    s = get_conn()
    s.send(st)
    #print 'sending:', st 
    data = s.recv(4096).decode()
    if debug:
        print data

def put_int():
    send_string("PUT;foo;1;INT")

def get_int():
    send_string("GET;foo;;")

def putlist():
    send_string('PUTLIST;bar;a,b,c;LIST')

def append_string():
    send_string("APPEND;bar;d;STRING")

def getlist():
    send_string('GETLIST;bar;;')

def get_stats():
    send_string('STATS;;;',True)

def incr_int():
    send_string("INCREMENT;foo;;")

def del_int():
    send_string("DELETE;foo;;")

def not_impl_cmd():
    send_string("HELLO;foo;;",False)


def corrupt_1():
    send_string('GETLIST;bar;',True)   # missing ;


def corrupt_2():
    send_string('GETLIST;bar;));', True)   # more ))


commands = [put_int, get_int, putlist, append_string,getlist,  incr_int , del_int,not_impl_cmd, corrupt_1,corrupt_2]


for _ in range(1000):
    commands[randrange(len(commands))]()

get_stats()


