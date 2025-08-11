import flet as ft
import alta_usuario as usuarionuevo
import consulta_usuario as consultau
import registro_biomasa as bioenergia_nueva
import consulta_bioenergia as consulta_bio

def main(page: ft.Page):

    def agregar_usuario(e: ft.ControlEvent):
        page.clean()
        usuarionuevo.main(page)

    def consulta_us(e: ft.ControlEvent):
        page.clean()
        consultau.main(page)
    
    def agregar_bioenergia(e: ft.ControlEvent):
        page.clean()
        bioenergia_nueva.main(page)
        
    def consulta_bioenergia(e: ft.ControlEvent):
        page.clean()
        consulta_bio.main(page)

    # Configuración de la página
    page.title = "Menú principal"
    page.theme_mode = "light"
    page.assets_dir = "assets"
    page.fonts = {
        "Poppins": "fonts/Poppins-Regular.ttf"
    }
    page.theme = ft.Theme(font_family="Poppins") 
    page.appbar = ft.AppBar(
        title=ft.Text("Sistema de Gestión de Bioenergías de Tabasco"),
        leading=ft.Icon("energy_savings_leaf"),
        color="green",
        bgcolor="white",
    )
    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        image=ft.DecorationImage(
            src="/bio.jpg",  # Imagen local
            fit=ft.ImageFit.COVER,
            #opacity=0.7
        )
    )

    # Encabezado con imagen a la derecha
    encabezado = ft.SafeArea(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text(value="¡Bienvenido!", size=70, color=ft.Colors.WHITE),
                        ft.Text(value="¿Qué desea hacer?", size=70, color=ft.Colors.WHITE)
                    ],
                    alignment="center",
                    spacing=0.5
                ),
                ft.Container(
                    content=ft.Image(
                        src="/Tabasco.jpg",  
                        width=300,
                        height=130,
                        fit=ft.ImageFit.COVER,
                        border_radius=10
                    ),
                    alignment=ft.alignment.center
                )
            ],
            alignment="spaceBetween",
            vertical_alignment="center"
        )
    )

    # Contenedores individuales
    cont_agregar_bio = ft.Container(
        content=ft.Row(
            [
                ft.Image(src="/B1.jpg", width=120, height=120, border_radius=10, fit=ft.ImageFit.COVER),
                ft.Column(
                    [
                        ft.Text("Agregar bioenergía", size=20, weight="bold"),
                        ft.Text("Registre una nueva bioenergía en el sistema."),
                        ft.ElevatedButton("Ir", icon=ft.Icons.ARROW_OUTWARD_ROUNDED, bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE, on_click=agregar_bioenergia)
                    ],
                    spacing=5,
                    alignment="center",
                    horizontal_alignment="center"
                )
            ],
            alignment="center",
            spacing=20
        ),
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        padding=20,
        alignment=ft.alignment.center,
        width=500,  
        height=180
    )

    cont_consulta_bio = ft.Container(
        content=ft.Row(
            [
                ft.Image(src="/B2.jpg", width=120, height=120, border_radius=10, fit=ft.ImageFit.COVER),
                ft.Column(
                    [
                        ft.Text("Consultar bioenergía", size=20, weight="bold"),
                        ft.Text("Vea los registros existentes de bioenergía."),
                        ft.ElevatedButton("Ir", icon=ft.Icons.ARROW_OUTWARD_ROUNDED, bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE, on_click=consulta_bioenergia)
                    ],
                    spacing=5,
                    alignment="center",
                    horizontal_alignment="center"
                )
            ],
            alignment="center",
            spacing=20
        ),
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        padding=20,
        alignment=ft.alignment.center,
        width=500,  
        height=180
    )

    cont_agregar_usuario = ft.Container(
        content=ft.Row(
            [
                ft.Image(src="/U1.jpg", width=120, height=120, border_radius=10, fit=ft.ImageFit.COVER),
                ft.Column(
                    [
                        ft.Text("Agregar usuario", size=20, weight="bold"),
                        ft.Text("Registre un nuevo usuario en el sistema."),
                        ft.ElevatedButton("Ir", icon=ft.Icons.ARROW_OUTWARD_ROUNDED, bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE,on_click=agregar_usuario)
                    ],
                    spacing=5,
                    alignment="center",
                    horizontal_alignment="center"
                )
            ],
            alignment="center",
            spacing=20
        ),
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        padding=20,
        alignment=ft.alignment.center,
        width=500,  
        height=180
    )

    cont_consulta_usuario = ft.Container(
        content=ft.Row(
            [
                ft.Image(src="/U2.jpg", width=120, height=120, border_radius=10, fit=ft.ImageFit.COVER),
                ft.Column(
                    [
                        ft.Text("Consultar usuarios", size=20, weight="bold"),
                        ft.Text("Vea todos los usuarios registrados."),
                        ft.ElevatedButton("Ir", icon=ft.Icons.ARROW_OUTWARD_ROUNDED, bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE,on_click=consulta_us)
                    ],
                    spacing=5,
                    alignment="center",
                    horizontal_alignment="center"
                )
            ],
            alignment="center",
            spacing=20
        ),
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        padding=20,
        alignment=ft.alignment.center,
        width=500,  
        height=180
    )

    # Fila con dos columnas: izquierda (bioenergía) y derecha (usuarios)
    fila_botones = ft.Row(
        [
            ft.Column([cont_agregar_bio, cont_consulta_bio], spacing=20, alignment="center"),
            ft.Column([cont_agregar_usuario, cont_consulta_usuario], spacing=20, alignment="center")
        ],
        alignment="center",
        spacing=50
    )

    # Añadir a la página
    page.add(encabezado)
    page.add(fila_botones)
    page.update()
    
if __name__ == "__main__":
    ft.app(target=main)
