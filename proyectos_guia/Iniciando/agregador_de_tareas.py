import flet as ft 

def main(page: ft.Page):

    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Que necesitas hacer?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Agregar", on_click=add_clicked, visible=True) ]))

ft.app(target=main)