from driver import Driver


class Car (Driver):
    
    def __init__(self,driver,marca):
        self.driver = driver
        self.marca = marca

    def movecar (self,NumberDice):
        return NumberDice * 100

  
    def printmodel(self):
        return f'modelo: {self.marca}'
        

        

       
    
        
    