import datetime

class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso= datetime.datatime(2018, 6, 1)
        self.__lista_medicamentos=[]

    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verListamedicamentos(self):
        return self.__lista_medicamentos
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarListamedicamentos(self,n):
        self.__lista_medicamentos = n 



class sistemaV:
    def __init__(self):
        self.__lista_felinos = {}
        self.__lista_caninos = {}

    def verificarExiste(self,historia):
        if historia in self.__lista_felinos or historia in self.__lista_caninos:
            return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False

    def verNumeroFelinos(self):
        return len(self.__lista_felinos) 

    def verNumeroCaninos(self):
        return len(self.__lista_caninos) 

    def ingresarFelinos(self,mascota):
        self.__lista_felinos[mascota.verHistoria()] = mascota

    def ingresarCaninos(self,mascota):
        self.__lista_caninos[mascota.verHistoria()] = mascota

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        if historia in self.__lista_felinos:
            masc = self.__lista_felinos[historia]
            return masc.verFecha() 
        elif historia in self.__lista_caninos:
            masc = self.__lista_caninos[historia]
            return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        if historia in self.__lista_felinos:
            masc = self.__lista_felinos[historia]
                return masc.verListamedicamentos() 
        elif historia in self.__lista_caninos:
            masc = self.__lista_caninos[historia]
            return masc.verListamedicamentos()
        return None

    def eliminarMedicamento(self, historia, medicamentoborrado):
        if historia in self.__lista_felinos:
            mas = self.__lista_felinos[historia]
            med = mas.verListamedicamentos()
            for m in med: 
                if m.verNombrem() == medicamentoborrado:
                    del m
                    return True  #eliminado con exito
        elif historia in self.__lista_caninos:
            mas = self.__lista_caninos[historia]
            med = mas.verListamedicamentos()
            for m in med:
                if m.verNombrem() == medicamentoborrado:
                    del m
                    return True 
        return False 


class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombrem(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        