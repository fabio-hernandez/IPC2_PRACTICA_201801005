from colorama import Fore, init
init()

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
                    if direccion == '':
                        print(
                            Fore.LIGHTRED_EX+'Archivo no cargado, por favor carga primero un archivo'+Fore.RESET)
                    else:
                        self.procesamiento()
                elif eleccion == 3:
                    self.crearArchivo()
                elif eleccion == 4:
                    print(Fore.LIGHTMAGENTA_EX +
                          'Fabio Josué Hernández Martinez - 201801005 - IPC2 "D"')
                elif eleccion == 5:
                    print(Fore.LIGHTMAGENTA_EX+'Saliendo del sistema LNG')
                    flag = False
                else:
                    print(Fore.LIGHTRED_EX+'* Opción Inválida *'+Fore.RESET)

    