import flet as ft
import re


def main(page: ft.Page):
    page.title = "Formulario de registro - Versión 3"

    name_input = ft.TextField(label="Nombre", width=300)
    email_input = ft.TextField(label="Emial", width=300)

    def on_submit(e):
        name = name_input.value
        email = email_input.value

        if not name: 
            page.snack_bar = ft.SnackBar(ft.Text("El campo 'nombre' no puede estar vacio"))
            page.snack_bar.open = True
            page.update()
            return
        
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            page.snack_bar = ft.SnackBar(ft.Text("El correo electrónico no puede estar vacio"))
            page.snack_bar.open = True
            page.update()
            return
        
        print(f"Nombre: {name}, Correo: {email}")
        page.snack_bar = ft.SnackBar(ft.Text("Datos enviados a la consola"))
        page.snack_bar.open = True
        page.update()

    submit_button = ft.ElevatedButton("Enviar", on_click=on_submit)

    page.add(
        ft.Text("Formulario de registro", size=30, weight="bold", color="blue"),
        name_input,
        email_input,
        submit_button
    )

ft.app(target=main)