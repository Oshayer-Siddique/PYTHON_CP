print("class and object")
class Car:
	name = "Axio"
	color = "black"

	def start():
		print("starting the car")

print(Car.name)
print(Car.color)
Car.start()

print("again Class")
class Car:
	name = ""
	color = ""

	def start():
		print("starting the car")

Car.name = "Axio"
Car.color = "white"
print(Car.name)
print(Car.color)
Car.start()

print(dir(Car))


print("class and object")
class Car:
	name = ""
	color = ""
	def start(self):
		print("starting the car")

my_car = Car()
my_car.name = "Tesla"
print(my_car.name)
my_car.start()
print("Class and object amuls academy")
class person:
	def __init__(self,n):
		self.name = n
		n = "John"
		print(n)
	def display(self):
		print("Hell0",self.name)

person1 = person("Amul")
person2 = person("Oshayer")
person1.display()
person2.display()
