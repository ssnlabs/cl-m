from xmlrpc.server import SimpleXMLRPCServer
def greet(name):
    return f"Hello, {name}!"
server = SimpleXMLRPCServer(("localhost", 8000))
print("RPC server listening on port 8000...")
server.register_function(greet, "greet")
server.serve_forever()
