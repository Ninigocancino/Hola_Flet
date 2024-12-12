import flet as ft

def main(page: ft.Page):
    page.title="Cajas concentricas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #page.spacing= 40

    aglutinado = ft.Stack(
          
          controls=[
                    ft.Container(
                    content=ft.Column(
                    controls=[],
                    width=800,
                    height=600,
                    ),
                    bgcolor=ft.colors.BLUE_400
                    ),

                    ft.Container(
                    content=ft.Column(
                    controls=[],
                    width=800,
                    height=600, 
                    ),
                    bgcolor=ft.colors.RED_400,
                    left=60,
                    right=60,
                    bottom=60,
                    ),

                    ft.Container(
                    content=ft.Column(
                    controls=[],
                    width=800,
                    height=600, 
                    ),
                    bgcolor=ft.colors.GREEN_400,
                    left=80,
                    right=80,
                    bottom=80,
                    ),

                    ft.Container(
                    content=ft.Column(
                    controls=[],
                    width=800,
                    height=600, 
                    ),
                    bgcolor=ft.colors.ORANGE_400,
                    left=120,
                    right=120,
                    bottom=120,
                    )
                ]
           
    )

    page.add(aglutinado)

ft.app(target=main)