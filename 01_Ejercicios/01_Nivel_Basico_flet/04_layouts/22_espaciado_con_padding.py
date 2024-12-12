import flet as ft

def main(page: ft.Page):
    page.title="Espaciado con Padding"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #page.spacing= 40
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
                    #padding=120
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
                    #padding=20
                    ),
                ]     
    )

    page.add(fila_1,fila_2)

ft.app(target=main)