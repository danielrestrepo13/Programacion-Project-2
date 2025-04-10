import datetime

class Reserva:
    """ Clase para representar una reserva de la cancha. 
        Tendrá estos atributos:
        __id (str): Identificador único de la reserva.
        __cliente (Cliente): Cliente que realiza la reserva.
        __cancha (Cancha): Cancha reservada.
        __fecha (datetime): Fecha de la reserva.
        __hora (str): Hora de la reserva en formato "HH:00".
    """
    # Variable para contar los ID únicos por reserva
    __contador_id = 0

    def __init__(self, cliente, cancha, fecha, hora):
        Reserva.__contador_id += 1
        self.__id = f"R{Reserva.__contador_id:04d}"
        self.__cliente = cliente
        self.__cancha = cancha
        self.__fecha = fecha
        self.__hora = hora

    
    # Getters
    def get_id(self):
        return self.__id
    
    def get_cliente(self):
        return self.__cliente
    
    def get_cancha(self):
        return self.__cancha
    
    def get_fecha(self):
        return self.__fecha
    
    def get_hora(self):
        return self.__hora
    
    def get_info(self):
        """ Retorna la información detallada de la reserva. """
        # Verificar si es tarifa nocturna
        es_nocturna = self.__cancha.es_horario_nocturno(self.__hora)
        precio = self.__cancha.get_costo(self.__hora)

        # Convertir la hora a formato más amigable
        hora_inicio = int(self.__hora.split(":")[0])
        hora_fin = hora_inicio + 1

        info = (f"ID: {self.__id}, Cliente: {self.__cliente.get_nombre()}, "
                f"Cancha: {self.__cancha.get_nombre()}, "
                f"Fecha: {self.__fecha.strftime('%d/%m/%Y')}, "
                f"Hora: {hora_inicio}:00 a {hora_fin}:00")
        
        if es_nocturna:
            info += f" - 💰 ${precio} (Tarifa nocturna)"
        else:
            info += f" - 💰 ${precio}"
        
        return info
    
    def cancelar(self):
        """ Cancela la reserva, liberando el horario en la cancha. """
        self.__cancha.cancelar_reserva(self.__hora)
        return True
    
    def mostrar_info(self):
        """ Mostramos la información completa de la reserva. """
        print("=" * 50)
        print("🎫 DETALLES DE RESERVA 🎫")
        print(f"🔢 ID: {self.__id}")
        print(f"👤 Cliente: {self.__cliente.get_nombre()} (ID: {self.__cliente.get_identificacion()})")
        print(f"🏟️ Cancha: {self.__cancha.get_nombre()}")
        print(f"📅 Fecha: {self.__fecha.strftime('%d/%m/%Y')}")

        # Convertir la hora a formato más amigable
        hora_inicio = int(self.__hora.split(":")[0])
        hora_fin = hora_inicio + 1

        print(f"⏰ Horario: {hora_inicio}:00 a {hora_fin}:00")

        # Verificar si es tarifa nocturna
        es_nocturna = self.__cancha.es_horario_nocturno(self.__hora)
        precio = self.__cancha.get_costo(self.__hora)

        if es_nocturna:
            print(f"💰 Costo: ${precio} (Tarifa nocturna)")
        else:
            print(f"💰 Costo: ${precio}")
        
        print("=" * 50)

        