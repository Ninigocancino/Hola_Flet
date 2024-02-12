import flet as ft
import time

def main(page: ft.Page):

    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    t = ft.Text(value="Hola Mundo!!!", color= "red")
    page.controls.append(t)
    page.update()


    #Esto hace que se muestre en panatalla un iterador, pero el mensaje 'Hola Mundo!!!' anterior deja de mostrarse  

    for i in range(10):
        t.value = f"Paso {i}"
        page.update()
        time.sleep(1)

ft.app(target=main)