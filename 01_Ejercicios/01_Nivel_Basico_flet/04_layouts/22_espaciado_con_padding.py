import flet as ft

def main(page: ft.Page):
    page.title="Espaciado con Padding"
    page.padding=200

    texto_2 = ft.Text("Texto 2")

    fila_1 = ft.Row(
          
          controls=[
                    ft.Container(
                    content=ft.Column(
                    controls=[],
                    width=200,
                    height=100
                    ),
                    bgcolor=ft.colors.BLUE_400,
                    ),
                ]     
    )

    fila_2 = ft.Row(
          
          controls=[
                    ft.Container(
                    content=ft.Column(
                    controls=[
                        texto_2
                    ],
                    width=200,
                    height=100
                    ),
                    bgcolor=ft.colors.BLUE_100,
                    ),
                ]     
    )

    page.add(fila_1,fila_2)

ft.app(target=main)