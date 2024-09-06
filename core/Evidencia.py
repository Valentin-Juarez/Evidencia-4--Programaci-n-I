#Crear un programa que tenga una clase soldador, con los atributos(Estado,Temperatura,TiempodeEncendido).
#Generar metodos que permitan ver el estado del objeto , Su temperatura y El tiempo.
#Ademas de que especifique si el objeto sufre de Sobrecalentamiento.

class Soldador_Vidral():
    def __init__(self,Temperatura,Tiempo):
        self.__Estado = "Apagado"
        self.__Temperatura = Temperatura
        self.TiempodeEncendido = Tiempo


    def get_Estado(self):
        return self.__Estado
    
    def get_Temperatura(self):
        return self.__Temperatura
    
    def set_Estado(self,Estado):
        self.__Estado = Estado
    
    def set_Temperatura(self,Temperatura):
        self.__Temperatura = Temperatura

    def __str__(self,Encender):
        if isinstance(Encender, str):
            if (Encender == "Encender" or Encender == "ENCENDER"):
                Sold_1.set_Estado = Encender
                return "El Soldador esta Encendido"
            else:
                raise ValueError ("Solo ingrese las opciones dadas")
        else:
            raise ValueError ("Ingrese solo letras")
    
    def Temperaturas(self,Grados):
        if (Sold_1.set_Estado != "Apagado"):
            if isinstance (Grados,int):
                if (Grados > 0 and Grados <= 450):
                    Sold_1.set_Temperatura = Grados
                    return Sold_1.set_Temperatura
                else:
                    raise ValueError ("Ingrese un valor menor a 450")
            else:
                raise ValueError ("Ingrese Solamente Numeros")
    def Tiempo_Max(self,Segundos,):
        Contador = 0
        while(Contador == 0):
            if (Segundos > 29):
                Contador +=1
                Sold_1.set_Estado = "Apagado"
                return ("El soldador se esta cerca de sobrecalentando y se Apagara")
                
            else:
                Segundos += 1
        
        
        
    
Sold_1=Soldador_Vidral(0,0)
#Encender = input("Hola, El soldador esta Apagado que desea hacer: Encender/Apagar: ")
#Grados = input("Ingrese la temperatura deseada:")