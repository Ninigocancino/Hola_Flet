import flet as ft

def main(page: ft.Page):
    page.title = "App con varias lineas de texto"
    linea_01 = ft.Text("Linea uno")
    linea_02 = ft.Text("Linea dos")
    linea_03 = ft.Text("Linea tres")
    linea_04 = ft.Text("Linea cuatro")

    page.add(linea_01,linea_02,linea_03,linea_04)

ft.app(target=main)