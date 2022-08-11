from track import Track
from driver import Driver
from car import Car
from dice import Dice


players = []
podium = []
cars = {}


def run():
    while True:
        print(
            """Bienvenido al juego de carreras.
        ESCOGE UNA OPCION: 

        1) Ingresa la cantidad de jugadores
        2) Ingresa la distancia de la pista
        3) A jugar
        4) Imprimir podio:
        5) Salir del juego """
        )

        opcion = int(input())
        if opcion == 1:

            print("ingresa la cantidad: ")
            countplayers = int(input())
            count = 1

            while countplayers != 0:
                name = input(f"ingresa el nombre del conductor # {count}: ")
                instan = Driver(name)
                model = input("ingrese la marca de su vehiculo: ")
                car = Car(instan.name, model)
                players.append(car)
                count += 1
                countplayers -= 1
                print(
                    f"se añadio el conductor {car.driver} para el vehiculo {car.marca}"
                )

            print(f"se añadieron con exito los {len(players)} conductores")
            print(
                """ 
            
             """
            )

        elif opcion == 2:

            distance = int(input("ingresa la distancia en KM: "))
            track = Track(distance)
            trackmetters = track.convertKmMetter()

            print(f"la distancia de la carrera es de {trackmetters} Mts")
            print(
                """ 
            
             """
            )

        elif opcion == 3:
            print("""A JUGAR""")
            distanceplayers = {}

            while len(podium) < 3:

                if len(podium) < 3:
                    print(" AUN NO LLEGADO NADIE ANIMO 🏎️🏎️🏎️")

                for i in players:

                    aleatorinumber = Dice.randomnumber()
                    movimentcar = i.movecar(aleatorinumber)
                    print(
                        f"sacaste {aleatorinumber} el vehiculo de {i.driver} avanzara {movimentcar} metros"
                    )

                    namedriver = i.driver

                    if namedriver in distanceplayers:
                        value = distanceplayers.get(namedriver)
                        actualice = value + movimentcar
                        distanceplayers.update({namedriver: actualice})
                        if actualice >= trackmetters:
                            podium.append(namedriver)
                            del distanceplayers[namedriver]
                    else:
                        distanceplayers[namedriver] = movimentcar

        elif opcion == 4:
            print(
                f""" FELICIDADES A LOS GANADORES: 🏎️🚀🚀🚀 
                 1er Lugar:  {podium[0]}
                 2do Lugar:  {podium[1]}  
                 3er Lugar:  {podium[2]}      """
            )

        elif opcion == 5:
            break

        else:
            print("escoge una opcion correcta")


if __name__ == "__main__":
    run()
