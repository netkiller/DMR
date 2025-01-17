#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("0.0.0.0", 50002))
print("UDP bound on port 50002...")
online = []

while True:
    data, addr = server.recvfrom(1024)
    print("%s:%s" % addr,end=" ")
    print(data)

    if addr not in online:
        online.append(addr)

    for ipaddr in online:
        server.sendto(data, ipaddr)
    # if data == b"exit":
    #     server.sendto(b"Good bye!\n", addr)
    #     continue
    # message = data.decode()
    # print(message)

	# 	message.encode()
    # server.sendto(b"Hello %s!\n" % data, addr)