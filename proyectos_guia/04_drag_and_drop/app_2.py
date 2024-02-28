import flet as ft 

def main(page: ft.Page):
    page.title= "Arrastrar y soltar"

    def drag_accept(e):
        #Trae el control 'draggable (de su origen) por su ID
        src = page.get_control(e.src_id)
        # Actualiza el texto dentro del control darggable después de arrastrar y soltar
        src.content.content.value = "0"
        # Actualiza el texto dentro del control objetivo después de arrastrar y soltar
        e.control.content.content.value = "1"
        page.update()

    page.add(
        ft.Row(
            [
                #Contenedor origen
                ft.Draggable(
                    group="numero",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.CYAN_200,
                        border_radius=10,
                        content=ft.Text("1", size=20),
                        alignment=ft.alignment.center,
                    ),
                    content_when_dragging=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.BLUE_GREY_200,
                        border_radius=5,
                    ),
                    content_feedback=ft.Text(":O")
                ),
                #Contenedor destino
                ft.Container(width=100),
                ft.DragTarget(
                    group="numero",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.PINK_200,
                        border_radius=5,
                        content=ft.Text("0", size=20),
                        alignment=ft.alignment.center,
                    ),
                    on_accept=drag_accept,
                ),
            ]
        )
    )

ft.app(target=main)