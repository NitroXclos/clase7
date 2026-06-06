class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"{self.nombre} - {self.telefono} - {self.email}"

contacto1 = Contacto("Alice", "123-456-7890", "alice@example.com")
print(contacto1)
contacto2 = Contacto("Bob", "987-654-3210", "bob@example.com")
print(contacto2) 

class producto: 
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - ${self.precio} - Cantidad: {self.cantidad}"
    
producto1 = producto("Laptop", 999.99, 10)
print(producto1) 