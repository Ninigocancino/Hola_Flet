import flet as ft
import re

def main(page: ft.page):
    page.title = "Formulario de registro - Versió 4"

    name_input = ft.TextField(label="Nombre", width=300)
    email_input = ft.TextField(label= "Correo electrónico", width= 300)
    age_input = ft.TextField(label="Edad", width=300)

    def on_submit(e):
        name = name_input.value
        email = email_input.value
        age = age_input.value


        if not name:
            page.snack_bar = ft.SnackBar(ft.Text("El campo nombre no pude estar vacio", color="red"))
            page.snack_bar.open = True
            page.update()
            return
        
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            page.snack_bar = ft.SnackBar(ft.Text("El formato no es correcto", color="red"))
            page.snack_bar.open=True
            page.update()
            return
        
        if not age.isdigit():
            page.snack_bar = ft.SnackBar(ft.Text("El campo 'edad' debe ser un digito", color="red"))
            page.snack_bar.open=True
            page.update()
            return
        
        with open("registro.txt", "a") as file:
            file.write(f"Nombre: {name}, Correo: {email}, Edad: {age}\n")

            page.snack_bar = ft.SnackBar(ft.Text("Datos guardados correctamente", color="Green"))
            page.snack_bar.open = True
            page.update()

    submit_button = ft.ElevatedButton("Enviar", on_click=on_submit)

    page.add(
        ft.Text("Formulario de registro", size=30, weight="bold", color= "blue"),
        name_input,
        email_input,
        age_input,
        submit_button
    )

ft.app(target=main)
        