import datetime
from cliente import Cliente
from cancha import CanchaSintetica, CanchaVoleyPlaya
from reserva import Reserva

class SistemaReservas:
    """ Clase principal que gestiona el sistema de reservas de las canchas. """
    def __init__(self):
        """ Inicia el sistema con las canchas creadas. """
        self.clientes = {} # Diccionario de clientes por identificación
        self.canchas = [CanchaSintetica(), CanchaVoleyPlaya()]
        self.reservas = []

    def registrar_cliente(self):
        """ Registrar un nuevo cliente en el sistema. """
        print("\n=== REGISTRO DE CLIENTE ===")
        nombre = input("Nombre: ")
        identificacion = input("Identificación: ")

        # Verificar si el cliente ya existe
        if identificacion in self.clientes:
            print("⚠️ ¡Este cliente ya se encuetra registrado!")
            return self.clientes[identificacion]
        
        celular = input("Celular: ")
        cliente = Cliente(nombre, identificacion, celular)
        self.clientes[identificacion] = cliente
        print(f"✅ Cliente {nombre} registrado correctamente.")
        return cliente
    
    def buscar_cliente(self):
        """ Buscar un cliente por su número de identificación. """
        print("\n=== BUSCAR CLIENTE ===")
        identificacion = input("Ingrese la identificación del cliente: ")
        
        if identificacion in self.clientes:
            return self.clientes[identificacion]
        
        print("⚠️ Cliente no encontrado.")
        return None
    
    def mostrar_canchas(self):
        """ Muestra la información de todas las canchas disponibles. """
        print("\n=== CANCHAS DISPONIBLES ===")
        for i, cancha in enumerate(self.canchas, 1):
            print(f"{i}.{cancha.get_nombre()}")
            print(f" 💰 ${cancha.get_costo()} por hora (hasta las 18:00)")
            print(f" 💰 ${cancha.get_costo_nocturna()} por hora (después de las 18:00)")

    def seleccionar_cancha(self):
        """ Permite al usuario seleccionar una cancha. """
        self.mostrar_canchas()
        try:
            opcion = int(input("\nSeleccione una cancha (número): "))
            if 1 <= opcion <= len(self.canchas):
                return self.canchas[opcion - 1]
            else:
                print("⚠️ Opción inválida.")
                return None
        except ValueError:
            print("⚠️ Por favor, ingrese un número válido.")
            return None
        
    def realizar_reserva(self):
        """ Proceso para realizar una nueva reserva. """
        print("\n=== REALIZAR RESERVA DE CANCHA ===")

        # Buscar o registrar cliente
        cliente = self.buscar_cliente()
        if not cliente:
            opcion = input("¿Desea registrar un nuevo cliente? (s/n): ")
            if opcion.lower() == 's':
                cliente = self.registrar_cliente()
            else:
                return
            
        # Seleccionar cancha
        cancha = self.seleccionar_cancha()
        if not cancha:
            return
        
        # Mostrar horarios de canchas disponibles en formato numerado
        print("\n⏰ Horarios disponibles:")
        if not cancha.mostrar_horarios():
            return
        
        # Seleccionar fecha y horario por número
        try:
            fecha_str = input("\nIngrese la fecha (DD/MM/YYYY): ")
            fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
            
            indice_horario = int(input("\nSeleccione el número del horario deseado: "))
            hora = cancha.reservar_horario_por_indice(indice_horario)
            
            if not hora:
                print("⚠️ Número de horario inválido.")
                return
            
            # Crear la reserva
            reserva = Reserva(cliente, cancha, fecha, hora)
            cliente.agregar_reserva(reserva)
            self.reservas.append(reserva)
            print("\n✅ ¡Reserva realizada con éxito!")
            reserva.mostrar_info()
        
        except ValueError:
            print("⚠️ Por favor, ingrese valores válidos.")

    def mostrar_reservas(self):
        """ Muestra todas las reservas realizadas. """
        print("\n=== TODAS LAS RESERVAS ===")
        if not self.reservas:
            print("⚠️ No hay reservas registradas.")
            return
        
        for i, reserva in enumerate(self.reservas, 1):
            print(f"{i}. {reserva.get_info()}")
    
    def mostrar_reservas_cliente(self):
        """ Muestra las reservas de un cliente específico. """
        cliente = self.buscar_cliente()
        if not cliente:
            return
        
        print(f"\n=== RESERVAS DE {cliente.get_nombre()} ===")
        if not cliente.reservas:
            print("⚠️ Este cliente no tiene reservas.")
            return
        
        for i, reserva in enumerate(cliente.reservas, 1):
            print(f"{i}. {reserva.get_info()}")

    def cancelar_reserva(self):
        """ Proceso para cancelar una reserva previa. """
        print("\n=== CANCELAR RESERVA ===")
        
        # Primero buscamos el cliente
        cliente = self.buscar_cliente()
        if not cliente or not cliente.reservas:
            print("⚠️ El cliente no tiene reservas para cancelar.")
            return
        
        # Mostrar las reservas del cliente
        print(f"\n🎫 Reservas de {cliente.get_nombre()}:")
        for i, reserva in enumerate(cliente.reservas, 1):
            print(f"{i}. {reserva.get_info()}")
        
        try:
            opcion = int(input("\nSeleccione la reserva a cancelar (número): "))
            if 1 <= opcion <= len(cliente.reservas):
                reserva = cliente.reservas[opcion - 1]
                
                # Cancelar la reserva
                reserva.cancelar()
                cliente.cancelar_reserva(reserva)
                self.reservas.remove(reserva)
                
                print("✅ Reserva cancelada con éxito.")
            else:
                print("⚠️ Opción inválida.")
        except ValueError:
            print("⚠️ Por favor, ingrese un número válido.")

    def mostrar_disponibilidad(self):
        """ Muestra la disponibilidad de horarios para todas las canchas. """
        print("\n=== DISPONIBILIDAD DE CANCHAS ===")
        for cancha in self.canchas:
            print(f"\n🏟️ {cancha.get_nombre()}:")
            cancha.mostrar_horarios()

    def menu_principal(self):
        while True:
            print("\n🏟️ SISTEMA DE RESERVAS DE CANCHAS DEPORTIVAS 🏟️")
            print("="*50)
            print("1. Realizar una reserva")
            print("2. Mostrar todas las reservas")
            print("3. Mostrar reservas de un cliente")
            print("4. Cancelar una reserva")
            print("5. Mostrar disponibilidad de canchas")
            print("6. Registrar nuevo cliente")
            print("7. Información de canchas")
            print("0. Salir")
            
            try:
                opcion = input("\nSeleccione una opción: ")
                
                if opcion == "1":
                    self.realizar_reserva()
                elif opcion == "2":
                    self.mostrar_reservas()
                elif opcion == "3":
                    self.mostrar_reservas_cliente()
                elif opcion == "4":
                    self.cancelar_reserva()
                elif opcion == "5":
                    self.mostrar_disponibilidad()
                elif opcion == "6":
                    self.registrar_cliente()
                elif opcion == "7":
                    self.mostrar_info_canchas()
                elif opcion == "0":
                    print("\n👋 ¡Gracias por usar el Sistema de Reservas de Canchas Deportivas!")
                    break
                else:
                    print("⚠️ Opción inválida.")
                
                input("\nPresione Enter para continuar...")
            
            except ValueError:
                print("⚠️ Por favor, ingrese un número válido.")
                input("\nPresione Enter para continuar...")
        
    def mostrar_info_canchas(self):
        """ Muestra información detallada de todas las canchas. """
        print("\n=== INFORMACIÓN DE CANCHAS ===")
        for cancha in self.canchas:
            cancha.mostrar_info()

def usuarios_prueba():
    """ Crea usuarios iniciales para pruebas del sistema. """
    # Clientes para probar el sistema
    clientes = [
    Cliente("Daniel García", "12345", "3101231230"),
    Cliente("Luisa Muñoz", "123456", "3101241240"),
    Cliente("Daniela Ussa", "1234567", "3101251250")
    ]

    return clientes



