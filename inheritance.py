class Parent:
    def __init__(self, name):
        self.name = name

    def parent_method(self):
        print(f"Parent called {self.name}")
        return "This is a method from the Parent class"


class Child(Parent):
    def childMethod(self, data):
        print('Child called', self.name)
        print('Received data:', data)


# Creating object
childobj = Child('MyParent')

# Child can access method of parent class
result = childobj.parent_method()
print(result)  # Optional: Print the returned value

# Call child method with data
childobj.childMethod('SampleData')
