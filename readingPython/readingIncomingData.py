
import socket

def readingData():
    try:
        s = socket.socket()
        host = socket.gethostname()
        port = 50009
        s.bind((host,port))
        s.listen(5)
        print 'Connecting ... '
        while True:
            print 'Waiting for data'
            c, addr = s.accept()
            print('Connection accepted from ' + repr(addr[1]))
            dataIncoming = c.recv(1026)
            stringdata = dataIncoming.decode('utf-8')
            if (dataIncoming != ""):
                print dataIncoming
                if (dataIncoming == "pick(grab)"):
                    print 'You are in!!! ' + dataIncoming
                else:
                    print 'Somting else'
            else:
                print 'Message incoming failed' + dataIncoming
            c.send('Server approved connection\n')
            print repr(addr[1]) + ": " + c.recv(1026)
            c.close()
    except (RuntimeError, TypeError, NameError, SyntaxError):
        print('Oops!  Something wrong')

if __name__ == "__main__":
    readingData()
