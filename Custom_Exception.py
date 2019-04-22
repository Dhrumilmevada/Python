class NegativeAgeException(RuntimeError):
    def __init__(self):
        super(NegativeAgeException,self).__init__()

def enterage(age):
	try:
		if age < 0:
			raise NegativeAgeException()
		elif age % 2 == 0:
			print("age is even")
		else:
			print("age is odd")
	
	except NegativeAgeException as ex:
	    print("Only positive integers are allowed",ex) 

num = int(input("Enter your age: "))   
enterage(num)
print('End')
