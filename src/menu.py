from tkinter import filedialog
from listaSimple import listaSimple
import xml.etree.ElementTree as ET
from item import Item
from colorama import Fore, init
init()

listaProductos = listaSimple()


class menu:

    def menu(self):
        contador = 0
        direccion = ''
        flag = True
        while flag:
            print(Fore.LIGHTCYAN_EX +
                  '-*-*-*-*-*-* GUATELAND S.A. *-*-*-*-*-*-' + Fore.WHITE)
            print('1. Cargar archivo para procesamiento')
            print('2. Obtener TOP 10 de productos con mayor margen de ganancias')
            print('3. Obtener TOP 10 de productos con mayor valor de inventario')
            print('4. Información del estudiante')
            print('5. Salir del sistema')
            try:
                eleccion = int(input(Fore.LIGHTYELLOW_EX+'>>>'))
                print(Fore.RESET)
            except ValueError:
                print(Fore.LIGHTRED_EX+'* Carácter No Valido *'+Fore.RESET)
            else:
                if eleccion == 1:
                    direccion = self.carga()
                    self.lector(direccion)
                    contador += 1
                elif eleccion == 2:
                    self.top10Ganancias()
                elif eleccion == 3:
                    self.top10Inventario()
                elif eleccion == 4:
                    print(Fore.LIGHTMAGENTA_EX +
                          'Fabio Josué Hernández Martinez - 201801005 - IPC2 "D"')
                elif eleccion == 5:
                    print(Fore.LIGHTMAGENTA_EX +
                          'Saliendo del sistema de GUATELAND S.A.')
                    flag = False
                else:
                    print(Fore.LIGHTRED_EX+'* Opción Inválida *'+Fore.RESET)

    def carga(self):
        ruta = filedialog.askopenfilename(title="Seleccione un archivo")
        file = open(ruta, "r", encoding="utf-8")
        file.close()
        print(Fore.GREEN+'Archivo cargado con éxito')
        return ruta

    def lector(self, ruta):
        tree = ET.parse(ruta)
        ItemList = tree.getroot()
        for item in ItemList.findall('Item'):

            codigo = item.find('ItemCode').text
            cantidad = float(item.find('QuantityOnHand').text)
            precio1 = float(item.find('PriceLevel1').text)
            precio2 = float(item.find('PriceLevel2').text)
            precio3 = float(item.find('PriceLevel3').text)
            costo = float(item.find('LastTotalUnitCost').text)
            margen1 = self.calcularMargenes(precio1, costo)
            margen2 = self.calcularMargenes(precio2, costo)
            margen3 = self.calcularMargenes(precio3, costo)
            valorInventario = self.calcularValorInventario(cantidad, costo)
            listaProductos.insertar(Item(codigo, cantidad, precio1, precio2,
                                         precio3, costo, margen1, margen2, margen3, valorInventario))

    def calcularMargenes(self, precio, costo):
        aux = precio-costo
        margen = (aux/costo)*100
        return margen

    def calcularValorInventario(self, cantidad, costo):
        valor = cantidad*costo
        return valor

    def top10Ganancias(self):
        print(Fore.LIGHTMAGENTA_EX +
              'Top 10 de productos con mayor margen de ganancia')
        print(Fore.GREEN + '---------------- Nivel 1 ----------------' + Fore.RESET)
        listaProductos.ordenar('Margen1')
        print(Fore.GREEN + '---------------- Nivel 2 ----------------' + Fore.RESET)
        listaProductos.ordenar('Margen2')
        print(Fore.GREEN + '---------------- Nivel 3 ----------------' + Fore.RESET)
        listaProductos.ordenar('Margen3')

    def top10Inventario(self):
        print(Fore.GREEN + 'Top 10 productos con mayor valor de Inventario' + Fore.RESET)
        listaProductos.ordenar('valorInventario')
