#!/usr/bin/env python
# -*- coding:utf-8 -*-


import serial.tools.list_ports

plist = list(serial.tools.list_ports.comports())


port_n = len(plist)

if port_n <= 0 :
	print 'no com port be found'
	exit()
else:
	print 'index\t' + 'describe'
	#print plist
	for i in range(port_n) :
		plist_x = list(plist[0])
		#print plist_x
		serialName = plist_x[0]
		print str(i) + '\tname >> ' + serialName



selectPort_n	= input('input index number select com port : ')
combaudrate		= input('set baudrate eg:115200 : ')
comprint		= input('print string or hex [S/H] : ')
comprint		= 'S'

combytesize = 8

comstopbits = 1

comtimeout = 2

comparity = 'N'

print ''
print ''
print "&-------------------------&"
print 'you have chosen number ',selectPort_n
print 'set baudrate at ',combaudrate
print 'bytesize ',combytesize
print 'stopbits ',comstopbits
print 'timeout ',comtimeout
print 'parity ',comparity
print 'print style ',comprint
print '&-------------------------&'

serialFd = serial.Serial(port = plist_x[selectPort_n],baudrate = combaudrate, bytesize=combytesize, parity=comparity, stopbits=comstopbits, timeout=comtimeout)


readlinestr = ''
while True:
	response = serialFd.readline()
	if len(response) > 0 :
		try:
			readlinestr = response.decode('utf-8')
		except Exception as e:
			readlinestr = ''
		else:
			print readlinestr



