class Item:

    codigo = str()
    cantidad = int()
    precio1 = int()
    precio2 = int()
    precio3 = int()
    costo = int()
    Margen1 = int()
    Margen2 = int()
    Margen3 = int()
    valorInventario = int()

    def __init__(self, codigo, cantidad, precio1, precio2, precio3, costo, Margen1, Margen2, Margen3, valorInventario):
        self.codigo = codigo
        self.cantidad = cantidad
        self.precio1 = precio1
        self.precio2 = precio2
        self.precio3 = precio3
        self.costo = costo
        self.Margen1 = Margen1
        self.Margen2 = Margen2
        self.Margen3 = Margen3
        self.valorInventario = valorInventario
