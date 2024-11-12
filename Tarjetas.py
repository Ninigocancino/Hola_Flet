import flet as ft

def main(page: ft.Page):
    page.title = "Tablero de tarjetas"
    page.padding = 20
    page.bgcolor = ft.colors.GREY_200

    def add_note(e):
        new_note = create_note("Nueva nota")
        grid.controls.append(new_note)
        page.update()

    def delete_note(note):
        grid.controls.remove(note)
        page.update()

    def create_note(text):
        note_content = ft.TextField(value=text,multiline=True,
                                        bgcolor=ft.colors.GREY_100)

        note = ft.Container(
            content=ft.Column([note_content, ft.IconButton(icon=ft.icons.DELETE,on_click=lambda _:delete_note(note))]),
        
            width=200,
            height=200,
            bgcolor=ft.colors.GREY_300,
            border_radius=10,
            padding=10,

        )

        return note
    
    grid = ft.GridView(
        expand=True,
        max_extent=220,
        child_aspect_ratio=1,
        spacing=10,
        run_spacing=10,
        #horizontal=False

    )
    
    notes = [
        "Comprar leche",
        "Llamar a mamá",
        "Reunión e las 3"
    ]


    for note in notes:
        grid.controls.append(create_note(note))

    page.add(ft.Row([
        ft.Text("Mis recordatorios", size=24, weight="bold",color=ft.colors.BLACK),
        ft.IconButton(icon=ft.icons.ADD, on_click=add_note, icon_color=ft.colors.BLACK)
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN), grid)


ft.app(target=main)
