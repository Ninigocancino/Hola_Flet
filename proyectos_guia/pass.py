#Veremos la estructura básica de una aplicación en Flet por lo que usaremos una función con un valor pass que disparará un elemento "control de carga/actualizar" al ejecutar el código

import flet as ft 

def main(page: ft.Page):

    pass

ft.app(target=main) #Muestra la ejecuación del código en una ventana del sistema operativo nativo 

#ft.app(target=main, view=ft.AppView.WEB_BROWSER) #Muestra la ejecución del código en el navegador por defecto de tu equipo