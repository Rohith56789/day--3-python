class Server:
    def __init__(self, name):
        self.name = name

    def start(self):
        return f"{self.name} is starting.."

    def deploy(self):
        return "Deploying web app using Parent Method"

# Apache Tomcat
class WebServer(Server):
    def deploy(self):
        return "Deploying web app using Child Method"
        # child is overriding the parent method

# Object creation and method calling (outside the class)
ws = WebServer("WebServer1")
print(ws.start())      # Output: WebServer1 is starting..
print(ws.deploy())     # Output: Deploying web app using Child Method
