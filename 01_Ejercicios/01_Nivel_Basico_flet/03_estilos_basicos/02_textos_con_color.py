import flet as ft

def main(page: ft.Page):

    page.title="Textos con color"
    color_red = ft.Text("Este es un tacxto de color Rojo", color=ft.colors.RED)
    color_red_100 = ft.Text( "Este es el color de texto red200", color=ft.colors.RED_100)

    page.add(color_red,color_red_100)

ft.app(target=main)