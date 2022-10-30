print("Class and Object")
class Car:
	def __init__(self,n,c,s):
		self.name = n
		self.color = c
		self.serial  = s

	def start(self):
		print("name:",self.name)
		print("color:",self.color)
		print("serial no",self.serial)
		print("starting The Engine")

my_car = Car("corolla","whte","123")
Car.start(my_car)
my_car1 = Car("Premio","Black","323")
Car.start(my_car1)

print("class and object 1")
class Movie:
	def __init__(self,n,t,c):
		self.name = n
		self.trailer = t
		self.code = c
	def film(self):
		print("name:",self.name)
		print("trailer:",self.trailer)
		print("Code:",self.code)
media = Movie("Harry potter","short","Magical")
Movie.film(media)

media1 =  Movie("ABC","large","Dance")
Movie.film(media1)


print("Class and Instance Variable")
class student:
	clg = "xyz"

	def __init__(self,r,n):
		self.roll = r
		self.name = n
	def display(self):
		print("Student Roll:",self.roll)
		print("student Name:",self.name)
		print("College name:",student.clg)


student1 = student("xyz001","Oshayer")
student.display(student1)
student2 = student("xyz002","rayan")
student.display(student2)

print("Inherritance")
class animal:
	def eating(self):
		print("eating")

class dog(animal):
	def bark(self):
		print("bark")

d = dog()
d.eating()
d.bark()
print("multilevel inheritance")
class person:
	def display(self):
		print("Hello A")

class employee(person):
	def printing(self):
		print("Hello B")

class programmer(employee):
	def show(self):
		print("Hello C")

p1 = programmer()
p1.display()
p1.printing()
p1.show()

print("Method Overriding")
class A:
	def display(self):
		print("Method of class A")

class B(A):
	def display(self):
		print("Method of class B")

b1 = B()
b1.display()
