import flet as ft


def main(page: ft.Page):
    page.title = "Alternativa B para crea Filas"
    page.vertical_alignment= ft.MainAxisAlignment.CENTER

    fila = ft.Row(
        controls=[
        ft.Text("Elemento 1"),
        ft.Text("Elemento 2"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=100
    )

    page.add(fila)

ft.app(target=main)