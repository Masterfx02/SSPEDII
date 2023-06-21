"""
    YESHUA NEFTALI ESPINOZA GONZÁLEZ 217586491
    SSPED II - INCO
    PRACTICA 3 - CIFRADO CAESAR SENCILLO
"""
def main():
    letras = "bcdefghijklmnopqrstuvwxyza" # Letras para el cifrado 
    
    try:
        archivo = open('cancion.txt', 'r') # Abre el archivo en modo lectura
        caracter = archivo.read(1)         # Lee el primer caracter del archivo
        nuevo_texto = "" # Variable para guardar el texto cifrado
        
        while caracter:
            if caracter != caracter.upper():   # Mientras haya caracteres para leer en el archivo
                try:  # Verificamos si el caracter no es una letra mayúscula
                    nuevo_texto += letras[letras.index(caracter) + 1] # índice del caracter en la cadena 'letras'
                    # Agregamos el caracter cifrado al texto nuevo
                except IndexError:
                    # Si hay un error de índice indica que el caracter es 'z', por lo tanto, se reemplaza por 'b'
                    nuevo_texto += 'b'
            else:
                # Si el caracter es una letra mayúscula, se agrega tal cual al texto nuevo
                nuevo_texto += caracter
            caracter = archivo.read(1)  # Lee el siguiente caracter del archivo

        print(nuevo_texto)  # Imprimimos el texto cifrado en la consola

        nuevo_archivo = open("cifrado.txt", mode="a+", encoding="utf-8")  # Abre y escribe  en un nuevo archivo
        nuevo_archivo.write(nuevo_texto)  # Escribimos el texto cifrado en el nuevo archivo
    except IOError:
        print('No se pudo abrir el archivo')
    finally:
        print('Fin del programa')
        archivo.close()
        # Cierra el archivo 'cancion.txt'

if __name__ == "__main__":
    main()
