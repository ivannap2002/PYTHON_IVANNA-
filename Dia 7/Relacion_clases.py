class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo_bruto):
        super().__init__(nombre, edad)
        if sueldo_bruto < 0:
            raise ValueError("El sueldo bruto no puede ser negativo")
        self.sueldo_bruto = sueldo_bruto

    def mostrar(self):
        super().mostrar()
        print(f"Sueldo Bruto: {self.sueldo_bruto:.2f}")
        print(f"Sueldo Neto: {self.calcular_salario_neto():.2f}")

    def calcular_salario_neto(self):
        # Calculo simplificado, en la realidad sería más complejo
        return self.sueldo_bruto * 0.85


class Directivo(Empleado):
    def __init__(self, nombre, edad, sueldo_bruto, categoria):
        super().__init__(nombre, edad, sueldo_bruto)
        self.categoria = categoria

    def mostrar(self):
        super().mostrar()
        print(f"Categoría: {self.categoria}")


class Cliente(Persona):
    def __init__(self, nombre, edad, telefono_de_contacto):
        super().__init__(nombre, edad)
        self.telefono_de_contacto = telefono_de_contacto

    def mostrar(self):
        super().mostrar()
        print(f"Teléfono de Contacto: {self.telefono_de_contacto}")


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.clientes = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def eliminar_empleado(self, nombre):
        self.empleados = [e for e in self.empleados if e.nombre != nombre]

    def eliminar_cliente(self, nombre):
        self.clientes = [c for c in self.clientes if c.nombre != nombre]

    def mostrar_empleados(self):
        print(f"Empleados de {self.nombre}:")
        if not self.empleados:
            print("No hay empleados en la empresa.")
        for empleado in self.empleados:
            empleado.mostrar()
            print()  # Línea en blanco para separar cada empleado

    def mostrar_clientes(self):
        print(f"Clientes de {self.nombre}:")
        if not self.clientes:
            print("No hay clientes en la empresa.")
        for cliente in self.clientes:
            cliente.mostrar()
            print()  # Línea en blanco para separar cada cliente


# Ejemplo de uso
empresa = Empresa("Mi Empresa")

# Creando empleados
empleado1 = Empleado("Juan", 30, 2500)
empleado2 = Directivo("Ana", 40, 4000, "Gerente")

# Agregando empleados a la empresa
empresa.agregar_empleado(empleado1)
empresa.agregar_empleado(empleado2)

# Creando clientes
cliente1 = Cliente("Pedro", 25, "1234567890")
cliente2 = Cliente("Maria", 35, "9876543210")

# Agregando clientes a la empresa
empresa.agregar_cliente(cliente1)
empresa.agregar_cliente(cliente2)

# Mostrar información
empresa.mostrar_empleados()
empresa.mostrar_clientes()
