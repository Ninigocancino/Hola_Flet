import flet as ft

def main(page: ft.Page):
    page.title="Colorear columna"
    page.vertical_alignment= ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing=10

    columna = ft.Container(
        content=ft.Column(
            controls=[],
            height=100,
            width=200
        ),
        bgcolor=ft.colors.BLUE_200,
    )

    columna2 = ft.Container(
        content=ft.Column(
            controls=[],
            height=100,
            width=200
        ),
        bgcolor=ft.colors.GREEN_100,
    )

    page.add(columna,columna2)
    

ft.app(main)