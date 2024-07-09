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
            print(f"El cliente {cliente.nombre} {cliente.apellido} nos ha vendido el vehículo {vehículo.marca} {vehículo.modelo} {vehículo.año} por {vehículo.precio}")
        
        else:
            print(f"El cliente {cliente.nombre} {cliente.apellido} no está registrado en el concesionario, por favor añadalo primero")

    #función venta de vehículo
    def venta_vehículo(self, vehículo, cliente):
        
        if cliente in self.clientes:
            self.inventario.remove(vehículo)
            print(f"El cliente {cliente.nombre} {cliente.apellido} ha comprado el vehículo {vehículo.marca} {vehículo.modelo} {vehículo.año}")

        else:
            print(f"El cliente {cliente.nombre} {cliente.apellido} no está registrado en el concesionario, por favor añadalo primero")


#Creando algunos clientes
cliente1 = cliente("Juan", "Pérez", "12345678A", "666777888")
cliente2 = cliente("María", "Gómez", "87654321B", "666777999")
cliente3 = cliente("Pedro", "Martínez", "12348765C", "666777000")

#Creando algunos vehículos
vehículo1 = vehículo("Audi", "A3", 2018, 20000, 50000, "Rojo", "Gasolina")
vehículo2 = vehículo("BMW", "Serie 3", 2019, 25000, 40000, "Azul", "Diésel")
vehículo3 = vehículo("Mercedes", "Clase A", 2017, 18000, 60000, "Blanco", "Gasolina")
vehículo4 = vehículo("BYD", "Song Plus", 2024, 50000, 10000, "Gris", "Híbrido")

#Creando el concesionario
concesionario = concesionario()

#Añadiendo clientes al concesionario
concesionario.añadir_cliente(cliente1)
concesionario.añadir_cliente(cliente2)
concesionario.añadir_cliente(cliente3)

#Inventario del concesionario
concesionario.inventario.append(vehículo1)
concesionario.inventario.append(vehículo2)

#Compra de vehículos
concesionario.comprar_vehiculo(vehículo3, cliente1)
concesionario.comprar_vehiculo(vehículo4, cliente2)

#Venta de vehículos
concesionario.venta_vehículo(vehículo1, cliente1)
concesionario.venta_vehículo(vehículo2, cliente3)

cliente3.consulta_inventario(concesionario)