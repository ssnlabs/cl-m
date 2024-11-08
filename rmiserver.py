import Pyro4

@Pyro4.expose
class RemoteService():
    def func(self,name):
        print("Hello: ",name)

Pyro4.Daemon.serveSimple({RemoteService:"remote"},ns=True)
