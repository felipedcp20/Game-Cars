class Track:

    def __init__(self,distancia):
        self.distancia = distancia
        
        
    def convertKmMetter(self):
        return (self.distancia*1000)

    def advance (self,finish,route):
        self.route  = route
        self.finish = finish
        counter = 0;
        if  counter >= finish :
            return True
        else:
            counter = counter + route
        

    
