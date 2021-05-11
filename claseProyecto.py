 
 
from os import putenv


class Proyecto:
    idProyecto=""
    titulo=""
    palabrasClave=""
    puntajes=0
    def __init__(self, idProyecto="", titulo="", palabrasClave="",puntajes=0):
        self.__idProyecto=idProyecto
        self.__titulo=titulo
        self.__palabrasClave=palabrasClave
        self.__puntajes=puntajes
    def __str__(self):
        return f"ID del Proyecto:{self.__idProyecto}\nTitulo:{self.__titulo}\nPalabras Clave:{self.__palabrasClave}\nPuntaje:{self.puntajes}\n"
    def obtenerID(self):
        return self.__idProyecto
    def __gt__(self,unPuntaje):
        band=None
        if self.__puntajes>unPuntaje.__puntajes: 
             band=True
        else: band=False 
        return band  #Retorna un valor booleano según la comparacion
    def ponerPuntaje(self,punt):
        self.__puntajes=punt
    #def ponerPuntaje(self, unPuntaje, idProyecto, proyectoControlador):
    #        unProyecto = Proyecto()
   #         listaProyectos = proyectoControlador.obtenerListaProyectos()
   #         for unProyecto in listaProyectos:
     #           if unProyecto.obtenerID() == idProyecto:
   #                 print(unPuntaje)
    #                self.puntaje = unPuntaje  
    #        print (self.puntaje)   
                         
                
    def mostrar(self):
        print (self.__idProyecto,self.__titulo,self.__palabrasClave)
        print ("El puntaje",self.__puntajes)

    def __eq__(self,ID_P):
        band=False
        if self.__idProyecto==ID_P:
            band=True
        return band
