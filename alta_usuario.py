import flet as ft
import airtable as at
def main(page: ft.Page):

    def guardar_usuario(e: ft.ControlEvent):
        clave = txt_clave.value
        contra = txt_contra.value
        contra2 = txt_contra2.value
        nombre = txt_nombre.value
        #Validar campos
        if clave == "":
            snackbar = ft.SnackBar(ft.Text("Introduce tu clave de usuario"), bgcolor="orange", show_close_icon=True)
            page.open(snackbar)
            return
        
        if contra == "":
            snackbar = ft.SnackBar(ft.Text("Introduce tu contraseña"), bgcolor="orange", show_close_icon=True)
            page.open(snackbar)
            return
        
        if contra2 == "":
            snackbar = ft.SnackBar(ft.Text("Introduce la confirmación de tu contraseña"), bgcolor="orange", show_close_icon=True)
            page.open(snackbar)
            return

        if nombre == "":
            snackbar = ft.SnackBar(ft.Text("Introduce tu nombre"), bgcolor="orange", show_close_icon=True)
            page.open(snackbar)
            return

        #Confirmar contraseña
        if contra != contra2:
            snackbar = ft.SnackBar(ft.Text("Contraseñas incorrectas"), bgcolor="red", show_close_icon=True)
            page.open(snackbar)
            return
        #Guardar el usuario en la nube
        nuevo = at.Usuario(
            clave=clave,
            contra=contra,
            nombre=nombre,
            admin=chk_admin.value,
        )
        try:
            nuevo.save()
            snackbar = ft.SnackBar(ft.Text("Usuario registrado"), bgcolor="blue", show_close_icon=True)
            page.open(snackbar)
        except Exception as error:
            snackbar = ft.SnackBar(ft.Text(error), bgcolor="red", show_close_icon=True)
            page.open(snackbar)

    #Configuración de la página
    page.title ="Altas"
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.window.width = 800
    page.window.height = 600
    page.appbar = ft.AppBar(
        title=ft.Text("Nuevo usuario"),
        center_title=True,
        leading=ft.Icon("person_add"),
        color="white",
        bgcolor="purple"
    )

    #Conponentes de la página
    txt_clave =ft.TextField(label="Clave del usuario", width=500)
    txt_contra =ft.TextField(label="Contraseña", width=500, password = True)
    txt_contra2 =ft.TextField(label="Confirmar contraseña", width=500, password = True)
    txt_nombre =ft.TextField(label="Nombre completo", width=500)
    chk_admin =ft.Checkbox(label="¿Es administrador?")
    fila_chk = ft.Row(
    controls=[chk_admin],
    alignment="center"
    )
    btn_guardar =ft.FilledButton(
        text="Guardar",
        icon="save",
        bgcolor="green",
        on_click=guardar_usuario
    )
    btn_cancelar = ft.FilledButton(
        text="Cancelar",
        icon="cancel",
        bgcolor="red"
    )
    
    fila = ft.Row(
        controls=[btn_guardar, btn_cancelar],
        alignment="center"
        )

    #Añadir componentes a la página
    page.add(txt_clave, txt_contra, txt_contra2, txt_nombre, fila_chk, fila)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)