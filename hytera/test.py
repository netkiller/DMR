#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("8.129.6.62", 50002)
# addr = ("127.0.0.1", 50002)
# addr = ("139.9.54.211", 50000)

# data, addr = s.recvfrom(1024)
# sleep(1)
# print(addr,data)

# 注册
s.sendto(b'P2P8\x01\x00\x00\x00\x14\x00\x00\x00\x08\x01\x01\x00\xe3\x07\x00\x00\x11\x00\x00\x00', addr)
data, addr = s.recvfrom(1024)
sleep(1)
print(addr,data)


# b'P2P8\x01\x00\x00\x00\x14\x00\x00\x007\xff\x01\x00\xe3\x07\x00\x00\x10\x00\x00\x00'
# data = b'\xbe\xbe\xbe\xbe\n\x00\x00\x00\x14\x00\x00\x00\xbe\xbe\xbd\xbe\xe3\x07\x00\x00'
# s.sendto(data, addr)

# data, addr = s.recvfrom(1024)
# s.sendto(b'P2P8/\x00\x00\x00\x00\x00\x00\x00\t\x01\x01\x00\x00\x00\x00\x00\x00',addr)
# sleep(1)
# print(addr,data)
#
