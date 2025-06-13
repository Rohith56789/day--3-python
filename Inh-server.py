class Server:
    def __init__(self, name):
        self.name = name

    def start(self):
        return f"{self.name} is starting.."


# Apache Tomcat
class WebServer(Server):
    def deploy(self):
        return f"Deploying web app on {self.name}"


# Jetty Server
class ApplicationServer(Server):
    def deploy(self):
        return f"Deploying application on {self.name}"


# Creating and using WebServer instances
ws1 = WebServer("WebServer1")
print(ws1.start())
print(ws1.deploy())

ws2 = WebServer("WebServer2")
print(ws2.start())
print(ws2.deploy())
