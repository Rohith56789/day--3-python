#my sample code
# class Server:
#     def __init__(self, host='localhost', port=8080):
#         self.host = host
#         self.port = port

#     def start(self):
#         print(f"Server started at {self.host}:{self.port}")

#     def stop(self):
#         print("Server stopped")


#creating an instance of the Server class
class Server:
    def __init__(self, serverId, name, ip, port):
        self.serverId = serverId
        self.name = name
        self.ip = ip
        self.port = port
        self.status = "offline"
        self.memory_usage = 0

    def ping(self):
        return f"Pinging {self.ip}....."

    def getStatus(self):
        return f"{self.name} status is {self.status}"

    def updateStatus(self):
        if self.status == "offline":
            self.status = "online"
        else:
            self.status = "offline"
        print(f"{self.name} status updated to {self.status}")


# Creating objects and calling methods
web_server1 = Server("S125451", "WebServer1", "192.168.1.10", 8080)
print(web_server1.ping())  # Output: Pinging 192.168.1.10.....
web_server2 = Server("S654665", "WebServer2", "192.168.1.11", 8081)
print(web_server2.ping())  # Output: Pinging 192.168.1.11.....

print(web_server1.getStatus())  # Output: WebServer1 status is offline
web_server1.updateStatus()
print(web_server1.getStatus())  # Output: WebServer1 status is online
