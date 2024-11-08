import xmlrpc.client
server = xmlrpc.client.ServerProxy("http://localhost:8000/")
name = "Alice"
result = server.greet(name)
print("Server response:", result)
