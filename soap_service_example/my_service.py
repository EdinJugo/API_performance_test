from spyne import ServiceBase, Application, rpc, Integer, String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
 
class OddOrEvenService(ServiceBase):
 
    @rpc(Integer, _returns=String)
    def oddOrEven(self, num):
        if num % 2 == 0:
            return "even"
        else:
            return "odd"
     
 
application = Application([OddOrEvenService], 'my.soap.app',
        in_protocol=Soap11(),
        out_protocol=Soap11(),
    )
 
wsgi_app = WsgiApplication(application)
server = make_server('127.0.0.1', 7789, wsgi_app)
 
print ("listening to http://127.0.0.1:7789")
print ("wsdl is at: http://localhost:7789/?wsdl")
 
server.serve_forever()