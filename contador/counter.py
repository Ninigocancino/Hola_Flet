import flet as ft
import time

#Funcionalidad del programa/app

def main(page:ft.Page):

#Función principal necesaria para poder crear el programa usando flet
    
    page.title = "Contador Flet" #Aquí agregamos el titulo de la pagina
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #Le dice a flet que posición debe tener el widget

    campo_numero = ft.TextField(value=f"0", text_align=ft.TextAlign.RIGHT, width=100) #En lavariable se utiliza el metodo 'ft.TextField' para crear un campo de texto que permita ingresar y mostrar un valor

    def reducir(evento):

        #Función que reduce el valor del campo de texto

        campo_numero.value = str(int(campo_numero.value) -1)
        campo_numero.update()

    def aumentar(evento):

        #Función que aumenta el valor del campo de texto

        campo_numero.value = str(int(campo_numero.value) + 1)
        campo_numero.update()

    #En esta parte controlamos la parte visual de la app
        
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click= reducir),
                campo_numero,
                ft.IconButton(ft.icons.ADD, on_click=aumentar),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

#Se llama a la función principal
ft.app(main)