import flet as ft 

def main(page: ft.Page):
    page.title="Colorear fila"
    page.spacing=5

    fila_1 = ft.Container(
        ft.Row(
        controls=[
        ]),
        bgcolor=ft.Colors.BLUE,
        height=50,
    )

    fila_2 = ft.Container(
        ft.Row(
        controls=[
        ]),
        bgcolor=ft.Colors.RED_100,
        height=100,
    )



    page.add(fila_1,fila_2)


ft.app(target=main)