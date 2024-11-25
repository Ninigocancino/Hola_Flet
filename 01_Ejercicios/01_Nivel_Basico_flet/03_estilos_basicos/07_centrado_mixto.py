import flet as ft

def main(page: ft.Page):
    page.title="Centrado Mixto"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    texto = ft.Text("Este texto se ubicará en el centro de la pantalla")

    page. add(texto)


ft.app(target=main)