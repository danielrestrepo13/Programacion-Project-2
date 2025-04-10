from sistema_reservas import SistemaReservas, usuarios_prueba

def main():
    """ Función principal para iniciar el sistema de reservas de canchas. """
    print("🏟️ Bienvenido al Sistema de Reservas de Canchas Deportivas 🏟️")
    print("=" * 50)
    print("💰 PRECIOS DE NUESTRAS CANCHAS:")
    print("⚽ Cancha Sintética: $40.000 por hora (hasta las 18:00)")
    print("⚽ Cancha Sintética: $45.000 por hora (después de las 18:00)")
    print("🏐 Cancha Vóley Playa: $50.000 por hora (hasta las 18:00)")
    print("🏐 Cancha Vóley Playa: $55.000 por hora (después de las 18:00)")
    print("=" * 50)
    print("⏰ Horario de funcionamiento: 10:00 a 22:00")
    print("=" * 50)

    # Crear el sistema
    sistema = SistemaReservas()

    # Cargar usuarios iniciales para la prueba
    clientes = usuarios_prueba()
    for cliente in clientes:
        sistema.clientes[cliente.get_identificacion()] = cliente

    # Iniciar el menú principal
    sistema.menu_principal()

if __name__ == "__main__":
    main()