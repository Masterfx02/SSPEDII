"""
    YESHUA NEFTALI ESPINOZA GONZÁLEZ 217586491
    SSPED II - INCO
    PRACTICA 1 - Vectores

    Mi ejemplo es sobre calcular la distancia recorrida en un viaje en carro.
    Los vectores son representados en dos distancias que ingresamos. 
"""
class DistanciaRecorrida:
    def __init__(self, distancia):   # Creamos un nuevo objeto de la clase
        self.distancia = distancia

    def suma(self, other):
        if isinstance(other, DistanciaRecorrida):  # Comprobamos si 'other' es una instancia de la clase DistanciaRecorrida.
            distancia_total = self.distancia + other.distancia # Sumamos las distancias
            return DistanciaRecorrida(distancia_total)  # Retorna la distancia total.
        else:
            print("El objeto a sumar debe ser una DistanciaRecorrida")
            # Si 'other' no es una instancia de la clase DistanciaRecorrida, imprime un mensaje de error.

    def Resultado(self):
        return f"Distancia recorrida: {self.distancia} km"


# Ingresamos las distancias de los tramos
tramo1 = float(input("Distancia recorrida en el primer tramo(km): "))
tramo2 = float(input("Distancia recorrida en el segundo tramo(km): "))

# Creamos los objetos de DistanciaRecorrida con las distancias ingresadas
distancia1 = DistanciaRecorrida(tramo1)
distancia2 = DistanciaRecorrida(tramo2)

# Sumamos las distancias recorridas
distancia_total = distancia1 + distancia2

# Imprime la distancia total recorrida en el viaje
print(distancia_total)
