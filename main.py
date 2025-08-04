import flet as ft
import alta_usuario as usuarionuevo
import consulta_usuario as consultau

def main(page: ft.Page):

    def agregar_usuario(e: ft.ControlEvent):
        page.clean()
        usuarionuevo.main(page)

    def consulta_us(e: ft.ControlEvent):
        page.clean()
        consultau.main(page)

    #Configuración de la página
    page.title = "Menú principal"
    page.theme_mode= "light"
    page.appbar = ft.AppBar(
        title= ft.Text("Sistema de Gestión de Bioenergías"),
        leading= ft.Icon("energy_savings_leaf"),
        color= "white",
        bgcolor= "purple",  
    )

    btn_nuevo = ft.ElevatedButton("Agregar nuevo usuario", on_click=agregar_usuario)
    btn_consultas = ft.ElevatedButton("Consultar usuarios", on_click=consulta_us)
    #Añadir a la página
    page.add(btn_nuevo,btn_consultas)
    page.update()
    
if __name__ == "__main__":
    ft.app(target=main)