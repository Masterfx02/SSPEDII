"""
    YESHUA NEFTALI ESPINOZA GONZÁLEZ 217586491
    SSPED II - INCO
    PRACTICA 2 - ARCHIVOS
"""

def Escritura_Archivo():
    try:
        # Abre el archivo original en modo lectura
        archivo = open('archivo.txt','r')
        # Lee todas las líneas del archivo
        texto = archivo.readlines()
        # Creamos una nueva lista con las líneas del archivo original
        nuevo_texto = []
        for i in range(len(texto)):
            nuevo_texto += [texto[i]] + ['*\n']
        # Abre un nuevo archivo en modo escritura
        nuevo_archivo = open("archivo2.txt", mode="a+", encoding="utf-8")
        # Escribe las líneas modificadas en el nuevo archivo
        nuevo_archivo.writelines(nuevo_texto)
    except IOError:
        print('No se pudo abrir el archivo')
    finally:
        print('Fin del programa') # Cierra el archivo original

def main():
    try:
        # Abre el archivo en modo lectura
        archivo = open('archivo.txt','r')
        # Lee y muestra el contenido del archivo
        print(archivo.read())
    except IOError:
        print('No se pudo abrir el archivo')
    finally:
        print('Fin del programa')

if __name__ == '__main__':
    main()
