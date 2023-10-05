import tkinter as tk
from tkinter import messagebox

class BibliotecaDigital:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, autor):
        libro = {'Título': titulo, 'Autor': autor}
        self.libros.append(libro)

    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro['Título'] == titulo:
                self.libros.remove(libro)
                return True
        return False

    def mostrar_libros(self):
        for libro in self.libros:
            print(f"Título: {libro['Título']}, Autor: {libro['Autor']}")


class InterfazGrafica:
    def __init__(self, ventana):
        self.biblioteca = BibliotecaDigital()

        ventana.title("Biblioteca Digital")

        self.etiqueta_titulo = tk.Label(ventana, text="Título:")
        self.etiqueta_titulo.pack()

        self.entrada_titulo = tk.Entry(ventana)
        self.entrada_titulo.pack()

        self.etiqueta_autor = tk.Label(ventana, text="Autor:")
        self.etiqueta_autor.pack()

        self.entrada_autor = tk.Entry(ventana)
        self.entrada_autor.pack()

        self.boton_agregar = tk.Button(ventana, text="Agregar libro", command=self.agregar_libro)
        self.boton_agregar.pack()

        self.boton_eliminar = tk.Button(ventana, text="Eliminar libro", command=self.eliminar_libro)
        self.boton_eliminar.pack()

        self.boton_mostrar = tk.Button(ventana, text="Mostrar libros", command=self.mostrar_libros)
        self.boton_mostrar.pack()

    def agregar_libro(self):
        titulo = self.entrada_titulo.get()
        autor = self.entrada_autor.get()

        if titulo and autor:
            self.biblioteca.agregar_libro(titulo, autor)
            messagebox.showinfo("Biblioteca Digital", "Libro agregado correctamente.")
            self.entrada_titulo.delete(0, tk.END)
            self.entrada_autor.delete(0, tk.END)
        else:
            messagebox.showerror("Biblioteca Digital", "Debes ingresar el título y el autor del libro.")

    def eliminar_libro(self):
        titulo = self.entrada_titulo.get()

        if titulo:
            if self.biblioteca.eliminar_libro(titulo):
                messagebox.showinfo("Biblioteca Digital", "Libro eliminado correctamente.")
            else:
                messagebox.showerror("Biblioteca Digital", "El libro no se encuentra en la biblioteca.")
            self.entrada_titulo.delete(0, tk.END)
        else:
            messagebox.showerror("Biblioteca Digital", "Debes ingresar el título del libro.")

    def mostrar_libros(self):
        libros = self.biblioteca.libros
        if libros:
            messagebox.showinfo("Biblioteca Digital", "Libros en la biblioteca:\n" +
                                '\n'.join([f"Título: {libro['Título']}, Autor: {libro['Autor']}" for libro in libros]))
        else:
            messagebox.showinfo("Biblioteca Digital", "No hay libros en la biblioteca.")


ventana_principal = tk.Tk()
interfaz = InterfazGrafica(ventana_principal)
ventana_principal.mainloop()
