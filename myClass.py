class Student:
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade
	def greet(self):
		print("Hello! My name is {}. I'm {} years old and am in grade {}.".format(self.name, self.age, self.grade))