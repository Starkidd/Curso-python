import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd= SocketServer.TCPServer(("",PORT),Handler)

print 'sirviendo en el puerto {0}'.format(PORT)

httpd.serve_forever()