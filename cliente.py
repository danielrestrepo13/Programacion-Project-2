class Cliente:
    """ Esta clase representa un cliente del complejo deportivo. 
    En sus atributos estarán todo lo requerido para su identificación y reserva """

    def __init__(self, nombre, identificacion, celular):
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__celular = celular
        self.reservas = [] # Lista pública dónde se mostrarán las reservas realizadas por el usuario

    
    # Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_identificacion(self):
        return self.__identificacion
    
    def get_celular(self):
        return self.__celular
    
    def agregar_reserva(self, reserva):
        """" Agrega una reserva a la lista de reservas del cliente. """
        self.reservas.append(reserva)
        return True
    
    def cancelar_reserva(self, reserva):
        """ Cancelar una reserva previa del cliente. """
        if reserva in self.reservas:
            self.reservas.remove(reserva)
            return True
        return False
    
    def mostrar_info(self): 
        """ Mostramos toda la información del cliente. """
        print("=" * 50)
        print(f"👤 Nombre: {self.__nombre}")
        print(f"🆔 Identificación: {self.__identificacion}")
        print(f"📱 Celular: {self.__celular}")
        print(f"🎫 Cantidad de reservas: {len(self.reservas)}")
        print("=" * 50)