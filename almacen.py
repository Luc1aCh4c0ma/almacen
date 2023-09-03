import tkinter as tk
from tkinter import ttk
import mysql.connector 

# Conexión a la base de datos
try:
    db_connection = mysql.connector.connect(user ='root', password= '123456', host = 'localhost',port='3306', database='almacen')

except mysql.connector.Error as error:
    print(f"Error de MySQL: {error}")

finally:
    if 'connection' in locals():
        db_connection.close()

# Función para cargar los productos
def cargar_productos():
    cursor = db_connection.cursor()
    cursor.execute("SELECT id_producto, nombre_producto FROM producto")
    productos = cursor.fetchall()
    db_connection.close()
    return productos

# Función para seleccionar el producto
def mostrar_caracteristicas():
    producto_seleccionado = combo_productos.get()
    if producto_seleccionado:
        db_connection.reconnect()
        cursor = db_connection.cursor()
        cursor.execute(f"SELECT nombre_producto, nombre_categoria, nombre_marca, precio_unitario, cantidad_disponible \
                        FROM producto \
                        JOIN categoria ON producto.id_categoria = categoria.id_categoria \
                        JOIN marca ON producto.id_marca = marca.id_marca \
                        JOIN precio ON producto.id_producto = precio.id_producto \
                        JOIN stock ON producto.id_producto = stock.id_producto \
                        WHERE producto.id_producto = {producto_seleccionado}")
        producto = cursor.fetchone()
        db_connection.close()
        if producto:
            resultado.config(text=f"Nombre: {producto[0]}\nCategoría: {producto[1]}\nMarca: {producto[2]}\nPrecio: {producto[3]}\nStock: {producto[4]}")
        else:
            resultado.config(text="Producto no encontrado")


# Crear la ventana principal
root = tk.Tk()
root.title("Consulta de Productos")

# Crear un combo box para seleccionar un producto
productos = cargar_productos()
combo_productos = ttk.Combobox(root, values=productos)
combo_productos.grid(row=0, column=0, padx=10, pady=10)

# Botón para mostrar características
btn_mostrar = tk.Button(root, text="Seleccionar", command=mostrar_caracteristicas)
btn_mostrar.grid(row=0, column=1, padx=10, pady=10)

# Etiqueta para mostrar las características del producto seleccionado
resultado = tk.Label(root, text="", justify="left")
resultado.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
