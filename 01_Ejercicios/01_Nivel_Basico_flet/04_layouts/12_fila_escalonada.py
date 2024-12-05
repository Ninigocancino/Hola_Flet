import flet as ft

def main(page: ft.Page):
    page.title="Filas escalonadas"


    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment= ft.CrossAxisAlignment.START
    
    elemento_1 = ft.Text(value="Elemento 1")
    elemento_2 = ft.Text(value="Elemento 2")
    elemento_3 = ft.Text(value="Elemento 3")

    fila_1 = ft.Row(
        controls=[
            elemento_1
        ],
        alignment=ft.MainAxisAlignment.START
    )

    fila_2 = ft.Row(
        controls=[
            elemento_2
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    fila_3 = ft.Row(
        controls=[
            elemento_3
        ],
        alignment=ft.MainAxisAlignment.END
    )

    page.add(fila_1, fila_2, fila_3)

ft.app(target=main)