class Parent:

    def __init__(self, name, serial):
        self.name = name
        self.serial = serial
	print ("self.name")

class ChildA(Parent):

    def __init__(self, a_name, a_serial, name ,sr):
        self.a_name = a_name
        self.a_serial = a_serial
        super().__init__(name,sr)

class ChildB(Parent):

    def __init__(self, b_name, b_serial,name,sr):
        self.b_name = b_namse
        self.b_serial = b_serial
        super().__init__(name,sr)


class GrandChild(ChildA, ChildB):
    def __init__(self):
        super().__init__(name = "blah", a_name = "a blah", b_name = "b blah", a_serial = 99, b_serial = 99, serial = 30)
