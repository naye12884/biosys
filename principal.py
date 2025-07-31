import flet as ft
#import registro_biomasa as reg
#import consulta_usuario as cons
def main (page: ft.Page):

    #def mostrar_registro(e: ft.ControlEvent):
        #page.clean()
        #reg.main(page)
    
    #def consulta(e: ft.ControlEvent):
        #page.clean()
        #cons.main(page)

    #Configuración de la página
    page.title = "Menú principal"
    page.theme_mode = "light"
    page.appbar = ft.AppBar(
        title=ft.Text("Sistema de Gestión de Bioenergías"),
        leading=ft.Icon("energy_savings"),
        color="white",
        bgcolor="purple"
    )
    #Componentes de la página
    btn_registro=ft.ElevatedButton("Registro")
    btn_consultas=ft.ElevatedButton("Consulta")
    page.add(btn_registro, btn_consultas)
    page.update()


if __name__== "__main__":
    ft.app(target=main)