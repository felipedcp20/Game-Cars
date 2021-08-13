players = []
car = []


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
             
             count +=1
             countplayers -=1

                

     elif opcion == 2:
        pass
     elif opcion == 3:
         pass
     elif opcion ==4:
         pass
     else:
         print("escoge una opcion correcta")
    

if __name__ == '__main__':
    run()