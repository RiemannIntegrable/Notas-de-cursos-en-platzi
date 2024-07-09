class vehículo:

    #constructor de la clase vehículo
    def __init__(self, marca, modelo, año, precio, kilometraje, color, combustible):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
        self.kilometraje = kilometraje
        self.color = color
        self.combustible = combustible

class cliente:

    #constructor de la clase cliente
    def __init__(self, nombre, apellido, dni, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono

    def consulta_inventario(self, concesionario):
        print("Inventario del concesionario:")
        for vehículo in concesionario.inventario:
            print(f"{vehículo.marca} {vehículo.modelo} {vehículo.año} {vehículo.precio}")

class concesionario:

    #constructor de la clase concesionario
    def __init__(self):
        self.inventario = []
        self.clientes = []

    #función añadir cliente
    def añadir_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Se ha añadido al cliente {cliente.nombre} {cliente.apellido}")

    #función compra de vehículo
    def comprar_vehiculo(self, vehículo, cliente):
        
        if cliente in self.clientes:
            self.inventario.append(vehículo)
            print(f"El cliente {cliente.nombre} {cliente.apellido} ha comprado el vehículo {vehículo.marca} {vehículo.modelo} {vehículo.año} por {vehículo.precio}")
        
        else:
            print(f"El cliente {cliente.nombre} {cliente.apellido} no está registrado en el concesionario, por favor añadalo primero")

    #función venta de vehículo
    def venta_vehículo(self, vehículo, cliente):
        
        if cliente in self.clientes:
            self.inventario.remove(vehículo)
            print(f"El cliente {cliente.nombre} {cliente.apellido} ha vendido el vehículo {vehículo.marca} {vehículo.modelo} {vehículo.año}")

        else:
            print(f"El cliente {cliente.nombre} {cliente.apellido} no está registrado en el concesionario, por favor añadalo primero")


