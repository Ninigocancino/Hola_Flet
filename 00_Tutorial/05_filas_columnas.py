import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.title = "Mi Flet app con filas y columnas"
    texto1 = ft.Text(value= "Texto 1",size=24, color=ft.colors.ORANGE_100 )
    texto2 = ft.Text(value= "Texto 2", size=18, color=ft.colors.ORANGE_100)
    texto3 = ft.Text(value= "Texto 2", size=18, color=ft.colors.ORANGE_100)

    fila_textos = ft.Row(
        controls=[texto1,texto2,texto3],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
        )
    
    boton1 = ft.FilledButton(text="Botón 1")
    boton2 = ft.FilledButton(text="Botón 2")
    boton3 = ft.FilledButton(text="Botón 3")

    fila_botones= ft.Row(
        controls=[boton1,boton2,boton3],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )
    
    textos_columnas = [
        ft.Text(value="Columna 1 - fila 1", size=18, color=ft.colors.WHITE),
        ft.Text(value="Columna 1 - fila 2", size=18, color=ft.colors.WHITE),
        ft.Text(value="Columna 1 - fila 3", size=18, color=ft.colors.WHITE),
    ]

    columna_texto1 = ft.Column(
        controls=textos_columnas
    )

    textos_columnas2 = [
        ft.Text(value="Columna 2 -fila 1", size=18, color=ft.colors.WHITE),
        ft.Text(value="Columna 2 - fila 2", size=18, color=ft.colors.WHITE),
        ft.Text(value="Columna 2 - fila 3", size=18, color=ft.colors.WHITE)
    ]

    columna_texto2 = ft.Column(
        controls=textos_columnas2
    )

    fila_columnas = ft.Row(
        controls=[columna_texto1, columna_texto2],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    page.add(fila_textos,fila_botones,fila_columnas)
    

ft.app(target=main)