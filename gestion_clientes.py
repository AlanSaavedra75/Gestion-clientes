import os
import json

class GestionClientes:
    DIRECTORIO_CLIENTES = "clientes"

    def __init__(self):
        # Asegurar que la carpeta exista
        if not os.path.exists(self.DIRECTORIO_CLIENTES):
            os.makedirs(self.DIRECTORIO_CLIENTES)

        # Diccionario hash para asociar nombres con archivos
        self.clientes = {}
        self.cargar_clientes()

    def cargar_clientes(self):
        """Carga los clientes desde los archivos existentes"""
        archivos = os.listdir(self.DIRECTORIO_CLIENTES)
        for archivo in archivos:
            if archivo.endswith(".json"):
                nombre_cliente = archivo.replace(".json", "")
                self.clientes[nombre_cliente] = os.path.join(self.DIRECTORIO_CLIENTES, archivo)

    def agregar_cliente(self):
        """Agrega un nuevo cliente"""
        nombre = input("Ingrese el nombre del cliente: ").strip()
        if nombre in self.clientes:
            print("⚠️ El cliente ya existe. Use la opción de modificar.")
            return

        servicio = input("Ingrese la descripción del servicio solicitado: ").strip()
        datos_cliente = {"nombre": nombre, "servicios": [servicio]}

        ruta_archivo = os.path.join(self.DIRECTORIO_CLIENTES, f"{nombre}.json")
        with open(ruta_archivo, "w") as archivo:
            json.dump(datos_cliente, archivo, indent=4)

        self.clientes[nombre] = ruta_archivo
        print(f"✅ Cliente '{nombre}' agregado correctamente.")

    def leer_cliente(self):
        """Muestra la información de un cliente"""
        nombre = input("Ingrese el nombre del cliente: ").strip()
        if nombre not in self.clientes:
            print("❌ Cliente no encontrado.")
            return

        with open(self.clientes[nombre], "r") as archivo:
            datos = json.load(archivo)
            print(json.dumps(datos, indent=4))

    def modificar_cliente(self):
        """Modifica la información de un cliente"""
        nombre = input("Ingrese el nombre del cliente a modificar: ").strip()
        if nombre not in self.clientes:
            print("❌ Cliente no encontrado.")
            return

        with open(self.clientes[nombre], "r") as archivo:
            datos = json.load(archivo)

        servicio_nuevo = input("Ingrese la nueva descripción del servicio: ").strip()
        datos["servicios"].append(servicio_nuevo)

        with open(self.clientes[nombre], "w") as archivo:
            json.dump(datos, archivo, indent=4)

        print(f"✅ Servicio agregado al cliente '{nombre}'.")

    def eliminar_cliente(self):
        """Elimina un cliente del sistema"""
        nombre = input("Ingrese el nombre del cliente a eliminar: ").strip()
        if nombre not in self.clientes:
            print("❌ Cliente no encontrado.")
            return

        os.remove(self.clientes[nombre])
        del self.clientes[nombre]
        print(f"🗑 Cliente '{nombre}' eliminado correctamente.")

    def menu(self):
        """Muestra el menú de opciones"""
        while True:
            print("\n📌 Menú de Clientes")
            print("1. Agregar Cliente")
            print("2. Leer Cliente")
            print("3. Modificar Cliente")
            print("4. Eliminar Cliente")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_cliente()
            elif opcion == "2":
                self.leer_cliente()
            elif opcion == "3":
                self.modificar_cliente()
            elif opcion == "4":
                self.eliminar_cliente()
            elif opcion == "5":
                print("👋 Saliendo del programa...")
                break
            else:
                print("❌ Opción inválida, intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    sistema = GestionClientes()
    sistema.menu()
