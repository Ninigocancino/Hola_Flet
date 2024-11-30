import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto integrador 02"
    page.horizontal_alignment = ft.CrossAxisAlignment.END
    page.padding = 20
    page.bgcolor = "ecede1"

    titulo = ft.Text(
        "¿Cómo orientar textos a \nla derecha usando Flet?",
        size=32,
        color="353a3b",
        weight="bold"
        )
    
    esp_1 = ft.Text(
        "",
        size=12
        )
    
    subtitulo = ft.Text(
        "Este articulo explora la forma más elemental\npara hacer que tus textos se orienten\nde derecha a izquierda en la ventana \nde previzualización de Flet",
        size=18,
        color= "353a3b",
        italic=True,
        )
    
    esp_2 = ft.Text(
        "",
        size=12
    )

    parrafo = ft.Text(
        "Crear texto y hacer que se muestre en pantalla de derecha\n a izquierda a través de una interfaz gráfica es muy sencillo\nen Flet.Para hacerlo unicamente debes crear un parametro\n global en la función 'main' usanda el control 'page.\nhorizontal_alignment' y pasarle como valor la setencia\n'ft.CrossAxisAlignment.EDN' que le indica a Flet que\nlos elementos dentro de la pagina se orientarán\n de derecha a Izquierda."
    )
    
    page.add(titulo,esp_1,subtitulo,esp_2,parrafo)


ft.app(target=main)