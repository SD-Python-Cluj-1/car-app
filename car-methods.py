class Car:

	def __init__(self, mark, color, fuel):
		self.mark = mark
		self.color = color
		self.fuel = fuel

	def display(self):
		print("This car is a", self.mark, self.color, "on", self.fuel) 