import flet as ft 

def main(page: ft.page):

    page.title = "Hola Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Row (
            [
                ft.Text("Hola mundo!!! esta es mi primer interacción con Flet", color="blue"),

            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    

ft.app(main)