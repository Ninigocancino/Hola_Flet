import flet as ft

def main(page: ft.Page):
    page.title="Fila inferior derecha"
    page.horizontal_alignment= ft.CrossAxisAlignment.END
    page.vertical_alignment = ft.MainAxisAlignment.END

    elemento_1 = ft.Text(value="Elemento 1")
    elemento_2 = ft.Text(value="Elemento 2")

    fila = ft.Row(
        controls=[
            elemento_1,
            elemento_2
        ],
        alignment=ft.MainAxisAlignment.END,
        spacing= 50
    )

    page.add(fila)

ft.app(target=main)