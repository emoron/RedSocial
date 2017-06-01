import os
from os import walk
from PIL import Image
from os import walk

'''
Recuerda que vamos a tener varios archivos en el proyecto
main.py que se encarga de crear la interfase donde se muestran las imagenes
imagen.py donde es la clase de imagen
clasificador.py que es el encargado de etiquetar las imagenes.
En la clase clasificador debe existir un diccionario llamado categorias
que contiene como llaves las diferentes etiquetas
Categorias={"perritos":[1,34,653]}

La lista de la categoria son los identificadores de las imagenes de esa categoria

Las imagenes se almacenan en una lista que contiene la ruta de  cada imagen y su identificador.

El directorio lo vamos a seleccionar desde la interfase de usuario (tkInter) y se lo vamos a pasar
a nuestro clasificador.


'''
ruta_deimagenes = os.getcwd()  # obtiene ruta del crpeta
contenido = os.listdir(ruta_deimagenes)
print (contenido)
for (ruta,carpeta,imagen) in os.walk(ruta_deimagenes):
    Lista_imagenes= []
    print (Lista_imagenes)
    lista=[]
    for i in (contenido):
           if i.endswith(('.png', '.pnj', '.gif')):
               mi_imagen= Image.open(ruta_deimagenes+'/'+ i)
               mi_imagen.show()
               for i in range(0,5):
                   lista.append(raw_input("ingresar etiquetas: "))

Numerodeosos=lista.count("oso")
print(Numerodeosos," son osos")
Numerodeperros=lista.count("perro")
print(Numerodeperros," son perros")
Numerodepersonas=lista.count("persona")
print(Numerodepersonas," son personas")
Numerodecasas=lista.count("casa")
print(Numerodecasas," son casas")
Numerodefotos=lista.count("foto")
print(Numerodefotos," son fotos")
Numerodecomputadoras=lista.count("computadora")
print(Numerodecomputadoras," son computadora")
Numerodepajaros=lista.count("pajaro")
print(Numerodepajaros," son pajaros")
Numerodearticulos=lista.count("articulo")
print(Numerodearticulos," son articulos")
                            
                            
                
#for (ruta, carpeta, imagen) in walk('ruta_deimagenes'):
   # print ruta
    #print carpeta
    #print imagen

 ##  Lista_carpeta = [carpeta]
    #Lista_imagen = [imagen]
   # print Lista_imagen
