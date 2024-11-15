import flet as ft

def main(page: ft.Page):
    page.title= "Mi primer parrafo con flet"
    parrafo = ft.Text("Este es mi primer parráfo usando Flet \nEn este ejercicio tu reto es crear cadena de caracteres \nque contenga saltos de lineas, de tal forma que un solo elemento \n o variable contenga todo el texto y evitando crear más de una variable \n para lograr el efecto de parráfo")

    page.add(parrafo)

ft.app(target=main)