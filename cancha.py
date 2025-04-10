class Cancha:
    """ 
    Clase base para representar una cancha del complejo deportivo.
    Tiene los atributos de nombre, tipo de cancha (sintética o vóley playa), costo x hora (incremento en tarifa nocturna) y los horarios disponibles.
    """

    def __init__(self, nombre, tipo, costo_hora, costo_hora_nocturna=None):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__costo_hora = costo_hora
        self.__costo_hora_nocturna = costo_hora_nocturna if costo_hora_nocturna is not None else costo_hora + 5000

        # Horarios disponibles de 10:00 am a 9:00 pm (último horario es de 9:00 a 10:00 pm)
        self.horarios_disponibles = [f"{hora}:00" for hora in range(10,22)]

    # Getters
    def get_nombre(self):
        """ Retorna el nombre de la cancha """
        return self.__nombre
    
    def get_tipo(self): 
        """ Retorna el tipo de cancha """
        return self.__tipo
    
    def get_costo(self, hora=None):
        """ Retorna el costo por hora de la cancha según el horario """
        if hora is None:
            return self.__costo_hora
        
        # Verificar si es horario nocturno (después de las 6:00 pm)
        hora_num = int(hora.split(":")[0])
        if hora_num >= 18: # 18:00 = 6:00 pm
            return self.__costo_hora_nocturna
        return self.__costo_hora
    
    def get_costo_nocturna(self):
        """ Retorna el costo por hora en tarifa nocturna """
        return self.__costo_hora_nocturna
    
    def es_horario_nocturno(self, hora):
        """ Verificar si una hora corresponde a tarifa nocturna """
        hora_num = int(hora.split(":")[0])
        return hora_num >= 18 # 18:00 = 6:00 pm

    def mostrar_horarios(self):
        """ Mostramos los horarios disponibles de las canchas en formato numerado """
        print(f"⏰ Horarios disponibles para {self.__nombre}:")
        if not self.horarios_disponibles:
            print("❌ No hay horarios disponibles para esta cancha.")
            return False
        
        for i, hora in enumerate(self.horarios_disponibles, 1):
            # Convertir la hora a un formato más amigable con el usuario
            hora_inicio = int(hora.split(":")[0])
            hora_fin = hora_inicio + 1

            # Verificar si es tarifa nocturna
            es_nocturna = self.es_horario_nocturno(hora)
            precio = self.get_costo(hora)

            # Mostrar horario con tarifa nocturna / si aplica
            if es_nocturna:
                print(f"{i}.{hora_inicio}:00 a {hora_fin}:00 - 💰 ${precio} (Tarifa nocturna)")
            else:
                print(f"{i}.{hora_inicio}:00 a {hora_fin}:00 - 💰${precio}")

        return True
    
    def reservar_horario_por_indice(self, indice):
        """ Reservar un horario escogiendo por índice en la lista de horarios disponibles."""

        if 1 <= indice <= len(self.horarios_disponibles):
            hora = self.horarios_disponibles.pop(indice - 1)
            return hora
        return None # Retorna None si el índice es inválido
    
    def reservar_horario(self, hora):
        """ Reservar un horario si está disponible """

        if hora in self.horarios_disponibles:
            self.horarios_disponibles.remove(hora)
            return True
        return False
    
    def cancelar_reserva(self, hora):
        """ Cancelar una reserva y volver a agregar el horario a los horarios disponibles. """
        if hora not in self.horarios_disponibles:
            self.horarios_disponibles.append(hora)
            self.horarios_disponibles.sort() # Ordenamos los horarios con sort (ordena los elementos de una lista en su lugar)

    def mostrar_info(self):
        """ Mostramos la información de la cancha. """
        print(f"🏷 Nombre: {self.__nombre}")
        print(f"🔖 Tipo de cancha: {self.__tipo}")
        print(f"💰 Costo por hora (hasta las 18:00): ${self.__costo_hora}")
        print(f"💰 Costo por hora (después de 18:00): ${self.__costo_hora_nocturna}")
        print(f"⏰ Horarios disponibles: {len(self.horarios_disponibles)}")
    
class CanchaSintetica(Cancha):
    """ Este clase se refiere a la cancha sintética y hereda de Cancha """

    def __init__(self):
        """ Iniciamos una cancha sintética con valores preestablecidos. Usamos super() para acceder a los métodos y propiedades de una clase padre. """
        super().__init__("Cancha Sintética", "Sintética", 40000)

    def mostrar_info(self):
        """ Sobreescribimos el método mostrar_info de la clase Cancha para mostrar la nueva información de esta cancha. """
        print("=" * 50)
        print("⚽ CANCHA SINTÉTICA ⚽")
        super().mostrar_info()
        print("🌱 Características: Césped artificial, ideal para fútbol")
        print("=" * 50)

class CanchaVoleyPlaya(Cancha):
    """ Este clase se refiere a la cancha vóley playa y hereda de Cancha """
    def __init__(self):
        """ Iniciamos una cancha con valores preestablecidos. """
        super().__init__("Cancha Vóley Playa", "Vóley Playa", 50000)

    def mostrar_info(self):
        print("=" * 50)
        print("🏐 CANCHA VÓLEY PLAYA 🏐")
        super().mostrar_info()
        print("🏖️ Características: Arena fina, red profesional")
        print("=" * 50)
