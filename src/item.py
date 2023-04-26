class Item:

    codigo = str()
    cantidad = int()
    precio1 = int()
    precio2 = int()
    precio3 = int()
    costo = int()
    margen1 = int()
    margen2 = int()
    margen3 = int()
    valorInventario = int()


    def __init__(self, codigo, cantidad, precio1, precio2, precio3, costo):
        self.codigo = codigo
        self.cantidad = cantidad
        self.precio1 = precio1
        self.precio2 = precio2
        self.precio3 = precio3
        self.costo = costo

    def calcularMargenes(self):
        print('margen')

    def calcularValorInventario(self):
        print('Valor')
