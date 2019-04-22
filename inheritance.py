class Car():
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

class ElectricCar(Car):
    def __init__(self, battery_type, model, color, mpg):
        self.battery_type=battery_type
        super().__init__(model, color, mpg)
	#Car.model=model
	#Car.color=color
	#Car.mpg=mpg

car = ElectricCar('battery', 'ford', 'golden', 10)
print (car.__dict__)
