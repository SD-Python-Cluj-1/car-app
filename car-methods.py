class Car:
    def __init__(self, year, make):
        pass
    
    def accelerate(self):
        self.speed += 10

    def decelerate(self):
        self.speed -= 10

    def get_speed(self):
        return self.speed
    
    def set_fuel_tank_capacity(self, tank):
        self.tank = tank
    
    def set_average_fuel_economy(self, fuel_economy):
        self.fuel_economy = fuel_economy
        
    def km_per_tank(self):
        return fuel_economy * tank
        
    
        
    