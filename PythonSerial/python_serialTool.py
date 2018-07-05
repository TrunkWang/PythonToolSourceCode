#!/usr/bin/env python
# -*- coding:utf-8 -*-


import serial.tools.list_ports


#****************************************
#
# global define
#
#****************************************
combaudrate = 115200
combytesize = 8
comstopbits = 1
comtimeout	= 2
comparity	= 'N'



#****************************************
#
# function define
#
#****************************************
def get_system_comlist():
	comlist = list(serial.tools.list_ports.comports())
	#print comlist
	return comlist

def show_comlist(plist ):
	if len(plist) <= 0 :
		return 0

	print 'index\tdescribe'
	for i in range(len(plist)):
		plist_x = list(plist[i])
		print str(i) + '\tname >> ' + plist_x[0]
	return i+1


def open_system_com(plist ):
	selectPort_n	= input('input com port index number : ')
	combaudrate		= input('set port baudrate eg:115200 : ')
	comprint		= input('print type str or hex [S/H] : ')
	comprint		= 'S'
	combytesize		= 8
	comstopbits		= 1
	omtimeout		= 2
	comparity		= 'N'

	plist_x = list(plist[selectPort_n])

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

	return serial.Serial(port = plist_x[0],baudrate = combaudrate, bytesize=combytesize, parity=comparity, stopbits=comstopbits, timeout=comtimeout)

def readline_com(serial_fd):
	response = serial_fd.readline()
	readlinestr = ''
	if len(response) > 0 :
		try:
			readlinestr = response.decode('utf-8')
		except Exception as e:
			readlinestr = '*com* can print'
	return readlinestr



#****************************************
#
# main proc
#
#****************************************

if __name__ == "__main__" :

	portlist = get_system_comlist()
	comcount = show_comlist(portlist)
	if comcount <= 0 :
		print 'error: no com ports be found'
		exit()
	serialFd = open_system_com(portlist)

	while True:
		readstr = readline_com(serialFd)
		if len(readstr) > 0 :
			print readstr

