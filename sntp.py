import socket
import struct
import time
import os

def sntp_info(server):
    client = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    client.settimeout(0.5)
    data = '\x1b' + 47 * '\0'
    try:
        client.sendto( data, (server, 123 ))
    except:
        return None, None
    data, address = client.recvfrom( 1024 )
    if data:
        return struct.unpack( '!12I', data )[10], address

def currenttime(offset = 0):
    TIME1970 = 2208988800L
    servers = ["{0}.pool.ntp.org".format(i) for i in xrange(0,4)]
    for s in servers:
        ct,address = 0,0
        try:
            ct,address = sntp_info(s)
        finally:
            return time.localtime(ct - TIME1970 + offset) if ct else None

if __name__ == "__main__":
    t = currenttime()
    
    print "Time = " + time.strftime("%H:%M:%S", t)
    print "Date = " + time.strftime("%m-%d-%Y", t)
