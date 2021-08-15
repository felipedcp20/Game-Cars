
from track import Track
from driver import Driver
from car import Car
from dice import Dice


players = []
podium = []
cars = {}



def run ():
    while True:   
        print("""Bienvenido al juego de carreras.
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
                model = input("ingrese la marca de su vehiculo: ")
                car = Car(instan,model)
                players.append(car)
                count +=1
                countplayers -=1
                print(f'se añadio el conductor {name} para el vehiculo {model}')
            
            print(f'se añadieron con exito los {len(players)} conductores')
            print(""" 
            
             """)
                    
                       
        elif opcion == 2:

            distance = int(input("ingresa la distancia en KM: "))
            track = Track(distance)
            trackmetters = track.convertKmMetter()
                
            print(f'la distancia de la carrera es de {trackmetters} Mts')
            print(""" 
            
             """)
                    
        
        
        elif opcion == 3:
            print("""A JUGAR""")
            objetc = []
            counter = []

            while (len(podium) <  3):
                
                for i in players:
                    aleatorinumber = Dice.randomnumber()
                    movimentcar = i.movecar(aleatorinumber)
                    print(f'sacaste {aleatorinumber} el vehiculo de  avanzara {movimentcar} metros')

                                     
                    if i in objetc:
                        
                        counter[i] = counter[i] + movimentcar
                    else:
                        objetc.append(i)
                        counter.append(i)

                    if (counter[i] >= trackmetters):
                        podium.append(objetc)
                    

                           
                     
                  

                   
                        
         
        elif opcion ==4:
            print(podium)
        elif opcion ==5:
            break

        else:
            print("escoge una opcion correcta")
    

if __name__ == '__main__':
    run()