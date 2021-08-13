from track import Track
from driver import Driver
from car import Car
from dice import Dice


players = []
podium = []
cars = {}





def run ():
        
    print("""Bienbenido al juego de carreras.
    ESCOGE UNA OPCION: 

    1) Ingresa la cantidad de jugadores
    2) Ingresa la distancia de la pista
    3) A jugar
    4) Imprimir podio: """)

    opcion = int(input())
    if opcion == 1:

        print("ingresa la cantidad: ")
        countplayers = int(input())
        count = 1
         

        while(countplayers != 0):
            name = input(f'ingresa el nombre del conductor # {count}: ')
            instan = Driver(name)
            players.append(instan)
            count +=1
            countplayers -=1

        print(f'se añadieron con exito los {len(players)} conductores')
         
        print  (players)
        for i in players:
            print(i.printdriver())


           

    elif opcion == 2:

        distance = int(input("ingresa la distancia en KM: "))
        track = Track(distance)
        trackmetters = track.convertKmMetter()
        
        
        print(f'la distancia de la carrera es de {trackmetters} Mts')
        
        
    elif opcion == 3:
        print("""A JUGAR""")
         
         
        while (len(podium) ==3):

            for i in players:
                pass
                                
                 
             
                       
         
        
         
    elif opcion ==4:
        pass

    else:
        print("escoge una opcion correcta")
    

if __name__ == '__main__':
    run()