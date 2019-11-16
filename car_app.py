import weather

class Car:
	def __init__(self, name, color, wheels):
		self.name = name
		self.color = color
		self.wheels = wheels
		self.accelerate = ''
		self.engine = ''

	def car(self):
		print("Car name: ", self.name)
		print("Car color: ", self.color)
		print("Car engine: ",self.engine)

# Our dashboard screen displays the weather!
# You can find 'w_details' in the module we imported

	def w_display(self):
		print(f"Let's see how the weather looks today:\n\n{weather.w_details}") 
