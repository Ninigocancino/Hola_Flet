import flet as ft

def main(page: ft.Page):
    page.title = "Galeria de productos responsiva"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.BLUE_GREY_900
    titulo = ft.Text(value="Galeria de productos", size=32,weight=ft.FontWeight.BOLD)
    
    page.add(titulo)

ft.app(target=main)