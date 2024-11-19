import flet as ft

def main(page: ft.Page):
    page.title = "Textos con tamaños"
    encabezado = ft.Text("Este es un encabezado de un contenido", size=60)
    subtitulo = ft.Text("Este es el subtitulo del contenido, es un texto más pequeño", size=20)
    parrafo = ft.Text("Este es un parrafo, es el más pequeños de los tres tipos de textos que estamos usando y además es el más extenso de ellos la intensión de una parrafo es dar mayor información al lector", size=12)

    page.add(encabezado,subtitulo,parrafo)

ft.app(target=main)

