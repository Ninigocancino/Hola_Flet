import flet as ft

def main(page: ft.Page):
    page.title = "Fila centro superior"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    elemento_1 = ft.Text(value="Elemento 1")
    elemento_2 = ft.Text(value="Elemento_2")

    fila = ft.Row(
        controls=[
            elemento_1,
            elemento_2
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    page.add(fila)

ft.app(target=main)