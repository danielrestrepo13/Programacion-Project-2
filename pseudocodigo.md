## Pseudocódigo – Sistema de Reservas de Canchas Deportivas
 
INICIO

CLASE Cliente
    ATRIBUTOS:
        nombre, identificacion, celular, reservas (lista)

    MÉTODOS:
        get_nombre()
        get_identificacion()
        agregar_reserva(reserva)
            AGREGAR reserva a la lista de reservas
        cancelar_reserva(reserva)
            REMOVER reserva de la lista de reservas
        mostrar_info()
            IMPRIMIR datos personales y cantidad de reservas

CLASE Cancha
    ATRIBUTOS:
        nombre, tipo, costo_hora, horarios_disponibles (lista)

    MÉTODOS:
        get_nombre()
        get_tipo()
        get_costo()
        mostrar_horarios()
            IMPRIMIR horarios_disponibles
        reservar_horario(hora)
            SI hora en horarios_disponibles
                REMOVER hora de horarios_disponibles
                RETORNAR VERDADERO
            SINO
                RETORNAR FALSO
        cancelar_reserva(hora)
            AGREGAR hora nuevamente a horarios_disponibles
        mostrar_info()
            IMPRIMIR nombre, tipo, costo y horarios disponibles

CLASE CanchaSintética HEREDA DE Cancha
    MÉTODO:
        mostrar_info() // sobrescribe
            IMPRIMIR "Cancha Sintética:" y llamar a mostrar_info() base

CLASE CanchaVóleyPlaya HEREDA DE Cancha
    MÉTODO:
        mostrar_info() // sobrescribe
            IMPRIMIR "Cancha Vóley Playa:" y llamar a mostrar_info() base

CLASE Reserva
    ATRIBUTOS:
        id, cliente, cancha, fecha, hora

    MÉTODOS:
        get_id()
        get_info()
            IMPRIMIR ID, cliente, cancha, fecha, hora
        cancelar()
            LLAMAR a cancha.cancelar_reserva(hora)
        mostrar_info()
            LLAMAR a get_info()

FUNCIÓN crear_cliente()
    PEDIR nombre, identificación, celular
    CREAR nuevo Cliente y RETORNAR

FUNCIÓN crear_cancha(tipo)
    SI tipo == "sintética"
        CREAR objeto CanchaSintetica con horarios y costo
    SINO SI tipo == "vóley-playa"
        CREAR objeto CanchaVoleyPlaya con horarios y costo
    RETORNAR cancha

FUNCIÓN realizar_reserva(cliente, cancha, fecha, hora)
    SI cancha.reservar_horario(hora) ES VERDADERO
        CREAR objeto Reserva con un ID único
        AGREGAR reserva al cliente
        IMPRIMIR "Reserva realizada con éxito"
    SINO
        IMPRIMIR "Horario no disponible"

FUNCIÓN cancelar_reserva(cliente, reserva)
    LLAMAR a reserva.cancelar()
    ELIMINAR reserva del cliente
    IMPRIMIR "Reserva cancelada"

FUNCIÓN principal()
    MOSTRAR opciones: crear cliente, ver canchas, hacer reserva, cancelar reserva, salir
    EJECUTAR según opción elegida

principal()

FIN
