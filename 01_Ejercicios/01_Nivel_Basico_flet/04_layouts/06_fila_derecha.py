import flet as ft

def main(page: ft.Page):
    page.title= "Fila derecha"
    page.horizontal_alignment= ft.CrossAxisAlignment.END

    elemento_1 = ft.Text(value="Elemento 1")
    elemento_2 = ft.Text(value="Elemento 2")

    fila = ft.Row(
        controls=[
            elemento_1,
            elemento_2,
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        spacing=20
    )

    page.add(fila)

ft.app(main)