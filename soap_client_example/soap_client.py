from zeep import Client
 
client = Client("http://localhost:7789/?wsdl")
print(client.service.oddOrEven(5))