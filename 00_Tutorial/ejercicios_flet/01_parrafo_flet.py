import flet as ft

def main(page: ft.Page):
    page.title = "Parrafo flet"
    page.bgcolor = ft.colors.GREY_200
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    encabezado = ft.Text("Flet un nuevo Framework Python", size=30)

    parrafo = ft.Text("Flet es una nueva forma para crear aplicaciones multiplataformas\nUsando Python, esto es una verdadera revolución en la forma de crear apps.\nSi ya programas en Python, pero siempre habías querido crear tus propias web\npero sin tener que aprender otro lenguaje entoces Flet es una gran opción para ti\n y ser uno de los primeros en trabajar con él puede ser algo interesante", text_align='CENTER')


    page.add(encabezado,parrafo)

ft.app(target=main)