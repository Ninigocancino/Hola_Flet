import flet as ft

def main(page: ft.Page):
    page.title = "Galeria de productos responsiva"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.BLUE_GREY_900


    titulo = ft.Text(value="Galeria de productos", size=32,weight=ft.FontWeight.BOLD)

    producto = ft.Container(
        content=ft.Row([
            ft.Text(value="Producto 1", size=16, weight=ft.FontWeight.BOLD),
            ft.Text(value="$19.99", size=14),
            ft.ElevatedButton(text="Agregar al carrito", color=ft.colors.WHITE)
        ]),
        bgcolor=ft.colors.BLUE_500,
        padding=20,
        width=1000,
        border_radius=20
        #expand=True
    )
    
    page.add(titulo, producto)

ft.app(target=main)