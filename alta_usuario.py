import flet as ft
import airtable as at
import main as menu_principal  # Para regresar al menú

def main(page: ft.Page):

    def guardar_usuario(e: ft.ControlEvent):
        clave = txt_clave.value
        contra = txt_contra.value
        contra2 = txt_contra2.value
        nombre = txt_nombre.value

        # Validar campos
        if clave == "":
            page.open(ft.SnackBar(ft.Text("Introduce tu clave de usuario"), bgcolor="orange", show_close_icon=True))
            return
        if contra == "":
            page.open(ft.SnackBar(ft.Text("Introduce tu contraseña"), bgcolor="orange", show_close_icon=True))
            return
        if contra2 == "":
            page.open(ft.SnackBar(ft.Text("Introduce la confirmación de tu contraseña"), bgcolor="orange", show_close_icon=True))
            return
        if nombre == "":
            page.open(ft.SnackBar(ft.Text("Introduce tu nombre"), bgcolor="orange", show_close_icon=True))
            return
        if contra != contra2:
            page.open(ft.SnackBar(ft.Text("Contraseñas incorrectas"), bgcolor="red", show_close_icon=True))
            return

        # Guardar el usuario en Airtable
        nuevo = at.Usuario(
            clave=clave,
            contra=contra,
            nombre=nombre,
            admin=chk_admin.value,
        )
        try:
            nuevo.save()
            page.open(ft.SnackBar(ft.Text("Usuario registrado"), bgcolor="blue", show_close_icon=True))
        except Exception as error:
            page.open(ft.SnackBar(ft.Text(error), bgcolor="red", show_close_icon=True))

    # Cancelar → limpia campos
    def cancelar(e):
        txt_clave.value = ""
        txt_contra.value = ""
        txt_contra2.value = ""
        txt_nombre.value = ""
        chk_admin.value = False
        page.update()

    # Regresar al menú
    def regresar_menu(e):
        page.clean()
        menu_principal.main(page)

    # Configuración de la página
    page.title = "Altas"
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.window.width = 800
    page.window.height = 600
    page.appbar = ft.AppBar(
        title=ft.Text("Nuevo usuario"),
        center_title=True,
        leading=ft.Icon("person_add"),
        color="white",
        bgcolor="green"
    )
    page.bgcolor = ft.Colors.WHITE

    # Componentes
    txt_clave = ft.TextField(label="Clave del usuario", width=500)
    txt_contra = ft.TextField(label="Contraseña", width=500, password=True)
    txt_contra2 = ft.TextField(label="Confirmar contraseña", width=500, password=True)
    txt_nombre = ft.TextField(label="Nombre completo", width=500)
    chk_admin = ft.Checkbox(label="¿Es administrador?")
    fila_chk = ft.Row(controls=[chk_admin], alignment="center")

    btn_guardar = ft.FilledButton(text="Guardar", icon="save", bgcolor="green", on_click=guardar_usuario)
    btn_cancelar = ft.FilledButton(text="Cancelar", icon="cancel", bgcolor="red", on_click=cancelar)
    btn_regresar = ft.FilledButton(text="Regresar al menú", icon="arrow_back", bgcolor="blue", on_click=regresar_menu)

    fila_botones = ft.Row(controls=[btn_guardar, btn_cancelar, btn_regresar], alignment="center")

    # Añadir a la página
    page.add(txt_clave, txt_contra, txt_contra2, txt_nombre, fila_chk, fila_botones)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
