import flet as ft

def main(page: ft.Page):
    page.title="Paddin en contenedores"
    #page.padding=200

    texto_2 = ft.Text("Texto 2")
    texto_1 = ft.Text("Texto 1")

    fila_1 = ft.Row(
          
          controls=[
                    ft.Container(
                    content=ft.Column(
                    controls=[
                        texto_1
                    ],
                    width=200,
                    height=100
                    ),
                    bgcolor=ft.colors.BLUE_400,
                    padding=40
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
                    padding=30
                    ),
                ]     
    )

    page.add(fila_1,fila_2)

ft.app(target=main)