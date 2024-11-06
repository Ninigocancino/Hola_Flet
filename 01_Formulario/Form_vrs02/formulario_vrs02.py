import flet as ft

def main(page: ft.page):
    page.title = "Formulario de registro - Versión 02"

    name_input = ft.TextField(label="Nombre", width=300)
    email_input = ft.TextField(label= "Email", width=300)

    def on_submit(e):
        print(f"Nombre: {name_input.value}, correo: {email_input}")
        page.snack_bar = ft.SnackBar(ft.Text("Datos enviados"))
        page.snack_bar.open = True
        page.update()

    submit_button = ft.ElevatedButton("Enviar", on_click=on_submit)

    page.add(
        ft.Text("Formulario de registro", size=30, weight="bold",color="blue"),
        name_input,
        email_input,
        submit_button
    )

ft.app(target=main)
