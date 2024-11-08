import flet as ft

def main(page: ft.Page):
    page.title = "Mi app con Flet"
    texto = ft.Text("Mi primera app programada con Python y Flet")
    page.add(texto)
    texto2 = ft.Text("Estoy coonstruyebdo mi primera aplicación en Flet")
    page.add(texto2)

ft.app(target=main)