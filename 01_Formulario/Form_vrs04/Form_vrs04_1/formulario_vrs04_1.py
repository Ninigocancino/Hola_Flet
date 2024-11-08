import flet as ft
import re
import os

def main(page: ft.Page):
    page.title = "Formulario de registro versión 4.1"

    name_input = ft.TextField(label="Nombre", width=300)
    email_input = ft.TextField(label="Email", width=300)
    age_input = ft.TextField(label="Edad", width=300)

    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "registro.txt")


    def on_submit(e):
        name = name_input.value
        email = email_input.value
        age = age_input.value

        if not name:
            page.snack_bar = ft.SnackBar(ft.Text("El campo nombre no puede estar vacio", color="red"))
            page.snack_bar.open = True
            page.update()
            return
        
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            page.snack_bar = ft.SnackBar(ft.Text("El formato de correo no es correcto", color="red"))
            page.snack_bar.open = True
            page.update()
            return
        
        if not age.isdigit():
            page.snack_bar = ft.SnackBar(ft.Text("El campo 'edad' debe ser un número", color="red"))
            page.snack_bar.open = True
            page.update()
            return
        
        with open(file_path, "a") as file:
            file.write(f"Nombre: {name}, Correo: {email}, Edad: {age}\n")

        
        page.snack_bar = ft.SnackBar(ft.Text("Datos guardado correctamente", color="green"))
        page.snack_bar.open= True
        page.update()

    submit_button = ft.ElevatedButton("Enviar", on_click=on_submit)

    page.add(
        ft.Text("Formulario de registro", size=30, weight="bold", color="blue"),
        name_input,
        email_input,
        age_input,
        submit_button
    )

ft.app(target=main)

