import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.GREY_200
    page.title = "Mi app con flet"
    texto = ft.Text("Esta es mi primera app con Python y Flet")
    page.add(texto)
    texto2 = ft.Text("Estoy construyendo mi primera aplicación con Python y Flet")
    page.add(texto2)

ft.app(target=main)